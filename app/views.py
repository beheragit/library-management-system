from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app.forms import BookForm, UserModelForm, UserLoginForm, AdminLoginForm
from app.models import AdminModel, UserModel, Book, IssuedBook
from datetime import datetime, timedelta
from django.contrib import messages

# 1. Home Page / Book List View
def first_page(request):
    books = Book.objects.all()
    user_role = request.session.get('user_role', None) 
    
    # Fetch the log list if an admin is looking at the homepage
    active_withdrawals = None
    if user_role == 'admin':
        active_withdrawals = IssuedBook.objects.filter(is_returned=False).select_related('user', 'book')
        
    return render(request, 'index.html', {
        'books': books, 
        'user_role': user_role,
        'active_withdrawals': active_withdrawals
    })

# 2. Handle Book Withdrawal (Fixed & Unified)
def withdraw_book(request, book_id):
    if request.session.get('user_role') != 'user':
        return redirect('/user-login/')
        
    session_username = request.session.get('username')
    
    try:
        student = UserModel.objects.get(user_username__iexact=session_username)
        book = Book.objects.get(bookid=book_id)
        
        if book.available_copies > 0:
            # Create transaction tracking log
            IssuedBook.objects.create(
                user=student,
                book=book,
                return_date=datetime.now().date() + timedelta(days=14)
            )
            
            # Deduct copy from inventory
            book.available_copies -= 1
            book.save()
            
            messages.success(request, f'Success! You withdrew "{book.bname}". Return deadline: {datetime.now().date() + timedelta(days=14)}')
        else:
            messages.error(request, f'Sorry, "{book.bname}" is completely out of stock right now.')
            
    except Exception as e:
        messages.error(request, f"SYSTEM ERROR: {str(e)}")
        
    return redirect('/')

# 3. New Admin Dashboard Page
def admin_dashboard(request):
    if request.session.get('user_role') != 'admin':
        return render(request, 'index.html', {'msg': 'Access Denied: Admins Only!'})
        
    active_issues = IssuedBook.objects.filter(is_returned=False).select_related('user', 'book')
    return render(request, 'admin_dashboard.html', {
        'active_issues': active_issues,
        'user_role': 'admin'
    })

# 4. Add Book View (Admin Only)
def create_book(request):
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

# 5. Admin Login
def admin_login_view(request):
    form = AdminLoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['admin_username']
        password = form.cleaned_data['admin_password']
        
        if AdminModel.objects.filter(admin_username__iexact=username, admin_password=password).exists():
            request.session['user_role'] = 'admin'  
            request.session['username'] = username
            request.session['display_name'] = 'Admin'
            return redirect('/')  
        else:
            msg = "Invalid Admin Credentials!"
            
    return render(request, 'login.html', {'form': form, 'login_type': 'admin', 'msg': msg})

# 6. User Login
def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['user_username'].strip()
        password = form.cleaned_data['user_password'].strip()

        user = UserModel.objects.filter(user_username__iexact=username, user_password=password).first()
        
        if user:
            request.session['user_role'] = 'user'  
            request.session['username'] = username
            request.session['display_name'] = user.user_name
            return redirect('/')  
        else:
            msg = "Invalid User Credentials!"
            
    return render(request, 'login.html', {'form': form, 'login_type': 'user', 'msg': msg})

# 7. User Registration View
def user_register_view(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully! Please Log In.')
            return redirect('/user-login/') 
    else:
        form = UserModelForm()
        
    return render(request, 'register.html', {'form': form})

# 8. Logout View
def logout_view(request):
    request.session.flush()  
    return redirect('/')