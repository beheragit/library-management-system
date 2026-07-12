from app.models import Book,AdminModel,UserModel
from django import forms
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class AdminModelForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        fields = ['admin_username', 'admin_password']
        widgets = {
            'admin_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Username'}),
            'admin_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Admin Password'}),
        }

class AdminLoginForm(forms.Form):
    admin_username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    admin_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),label="Password")

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        # Structural layout order on the web page
        fields = ['user_id', 'user_name', 'user_branch', 'user_username', 'user_password']
        
        # Explicitly change the text labels so they don't look confusing
        labels = {
            'user_name': 'Your Full Name',
            'user_username': 'Create Username (Login ID)',
            'user_branch': 'Branch/Department',
        }
        
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User ID'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lakshminarayana Behera'}),
            'user_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Branch'}),
            'user_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lnbehera'}),
            'user_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        }

class UserLoginForm(forms.Form):
    user_username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )