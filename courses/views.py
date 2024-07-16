from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView 
from django.db import transaction
from .models import *



class VideosListView(ListView):
    model = Course
    template_name = 'courses/videos.html'

    def get_queryset(self):
        # Use a transaction to ensure atomicity
        with transaction.atomic():
            # Get the queryset
            queryset = super().get_queryset()
            
            # Increment the views field for each object
            for obj in queryset:
                obj.views += 1
                obj.save()  # Save each object with the new value
            
        return queryset