from django.shortcuts import render
from django.views.generic import ListView 
from .models import *



class VideosListView(ListView):
    model = Course
    template_name = 'courses/videos.html'