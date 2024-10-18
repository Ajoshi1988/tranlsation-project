from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    
    path('user-logout', views.user_logout, name="user-logout" ),
    path('profile', views.profile, name="profile" ),
    
    path('password-reset-custom', views.PasswordReset, name="password_reset" ),
    
    
]