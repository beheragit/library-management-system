from django.db import models

# Create your models here.
class Book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    author_image=models.ImageField(upload_to='images/')
    book_file=models.FileField(upload_to='documents/')

class AdminModel(models.Model):
    admin_username = models.CharField(max_length=50, unique=True)
    admin_password = models.CharField(max_length=128)

class UserModel(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_branch = models.CharField(max_length=15, null=True, blank=True)
    user_username = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=128)
    
    