from django.urls import path
from .views import * 



app_name = 'courses'

urlpatterns = [
    path('',VideosListView.as_view(),name='videos'),
    path('search/',VideosSearchView,name='search'),
]
