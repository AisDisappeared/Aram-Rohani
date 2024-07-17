from django.urls import path 
from .views import * 



urlpatterns = [
    path('',indexview,name='home'),
]
