from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    
    path('translate', views.TranslatePage, name="translate"),
  
    

   
    path('download/', views.download_file, name='download_file'),
    
    
    
    
]