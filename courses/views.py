from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic import ListView 
from django.db import transaction
from django.db.models import Q
from .models import *



class VideosListView(ListView):
    model = Course
    template_name = 'courses/videos.html'
    paginate_by = 4

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
    


def VideosSearchView(request):
    allvideos = Course.objects.all()
    object_list = ''
    if request.method == 'GET':
        s = request.GET.get('s')
        if len(s) > 0:
            object_list = allvideos.filter(Q(title__contains=s) | Q(description__contains=s))
        else:
            return redirect(request.META.get('HTTP_REFERER'))
        
        context = {"object_list":object_list}
        return render(request,'courses/videos.html',context)
    
    return redirect(request.META.get('HTTP_REFERER'))
