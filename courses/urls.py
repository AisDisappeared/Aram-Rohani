from django.urls import path
from .views import * 


urlpatterns = [
    path('',VideosListView.as_view(),name='videos'),
]
