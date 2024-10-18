from django.urls import path
from .consumers import *

ws_urlpatterns=[
    
    path('ws/graph/', progressConsumer.as_asgi()),
    
   
]