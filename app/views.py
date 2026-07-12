from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from app.forms import BookForm,UserModelForm, UserLoginForm,AdminLoginForm
from app.models import AdminModel, UserModel, Book
from django.contrib import messages
# 1. Home Page / Book List View
def first_page(request):
    books = Book.objects.all()
    # Check what role is stored in the current session
    user_role = request.session.get('user_role', None) 
    
    return render(request, 'index.html', {
        'books': books,
        'user_role': user_role
    })

# 2. Add Book View (Admin Only)
def create_book(request):
    # Security Check: If they are not an admin, kick them back to home page
    if request.session.get('user_role') != 'admin':
        return render(request, 'index.html', {'msg': 'Access Denied: Admins Only!'})

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'booktemp.html', {'form': BookForm(), 'msg': 'BOOK IS MADE'})
    else:
        form = BookForm()
        
    return render(request, "booktemp.html", {"form": form})

# 3. Admin Login (Saves 'admin' to session)
def admin_login_view(request):
    form = AdminLoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['admin_username']
        password = form.cleaned_data['admin_password']
        
        if AdminModel.objects.filter(admin_username__iexact=username, admin_password=password).exists():
            request.session['user_role'] = 'admin'  # Set session
            request.session['username'] = username
            request.session['display_name'] = 'Admin'
            return redirect('/')  # Redirect to home page
        else:
            msg = "Invalid Admin Credentials!"
            
    return render(request, 'login.html', {'form': form, 'login_type': 'admin', 'msg': msg})


# 4. User Login (Saves 'user' to session)
def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST" and form.is_valid():
        # .strip() removes any accidental spaces typed at the beginning or end
        username = form.cleaned_data['user_username'].strip()
        password = form.cleaned_data['user_password'].strip()

        user = UserModel.objects.filter(user_username__iexact=username, user_password=password).first()
        
        # Using user_username__iexact makes the login case-insensitive (e.g., Lnbehera matches lnbehera)
        if UserModel.objects.filter(user_username__iexact=username, user_password=password).exists():
            request.session['user_role'] = 'user'  
            request.session['username'] = username
            request.session['display_name'] = user.user_name
            return redirect('/')  
        else:
            msg = "Invalid User Credentials!"
            
    return render(request, 'login.html', {'form': form, 'login_type': 'user', 'msg': msg})

# 5. User Registration View
def user_register_view(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success notification
            messages.success(request, 'Account Created Successfully! Please Log In.')
            # Redirect to the actual login URL path
            return redirect('/user-login/') 
    else:
        form = UserModelForm()
        
    return render(request, 'register.html', {'form': form})

# 6. Handle Book Withdrawal
def withdraw_book(request, book_id):
    if request.session.get('user_role') != 'user':
        return render(request, 'index.html', {
            'books': Book.objects.all(),
            'msg': 'Please log in as a User to withdraw books.'
        })
    
    # Using get_object_or_400 prevents code crashing if an invalid ID is passed
    book = get_object_or_404(Book, bookid=book_id)
    
    # Note: Link this book to the user in your database relationship table here if needed.
    return render(request, 'index.html', {
        'books': Book.objects.all(),
        'user_role': 'user',
        'msg': f'Successfully withdrew "{book.bname}"!'
    })

# 7. Optional Bonus: Logout View
def logout_view(request):
    request.session.flush()  # Completely clears session data
    return redirect('/')