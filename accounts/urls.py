from django.urls import path 
from .views import * 


urlpatterns = [
    path('login/',LoginView,name='login'),
    path('signup',RegisterView,name='register'),
    path('logout',LogoutView,name='logout'),
]