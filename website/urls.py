from django.urls import path 
from .views import * 


app_name = 'website'
urlpatterns = [
    path('',indexview,name='home'),
]
