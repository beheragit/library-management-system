"""
URL configuration for Project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import first_page,create_book,admin_login_view,user_login_view,user_register_view,withdraw_book,logout_view,admin_dashboard, return_book
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first_page),
    path('createbook/',create_book),
    path('admin-login/',admin_login_view),
    path('user-login/',user_login_view),
    path('register/', user_register_view),
    path('withdraw/<int:book_id>/', withdraw_book),
    path('admin-dashboard/', admin_dashboard),
    path('logout/', logout_view),
    path('return/<int:issue_id>/', return_book),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
