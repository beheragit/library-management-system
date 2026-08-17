from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    author_image=models.ImageField(upload_to='images/')
    book_file=models.FileField(upload_to='documents/')
    available_copies = models.IntegerField(default=10)

class AdminModel(models.Model):
    admin_username = models.CharField(max_length=50, unique=True)
    admin_password = models.CharField(max_length=128)

class UserModel(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_branch = models.CharField(max_length=15, null=True, blank=True)
    user_username = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=128)
#Tracks withdrawals, student details, and return period
class IssuedBook(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    # Default return period set to 14 days from today
    return_date= models.DateField(default=datetime.now().date() + timedelta(days=14))
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user_name} - {self.book.bname}"
    
    