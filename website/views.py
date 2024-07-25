from email.policy import default
from django.shortcuts import render
from courses.models import Course
from .forms import SubscribeForm
from decouple import config
import sweetify

def indexview(request):
    video = Course.objects.get(id=config('VID_ID',default=3))
    video.views += 1 
    video.save()
    context = {"specvideo":video}
    return render(request,'website/index.html',context)







def SubscribeView(request):
    if request.method == 'POST':
         form = SubscribeForm(request.POST)
         if form.is_valid():
            form.save()       
            sweetify.success(request,'Welcome to our community! Thank you for supporting',persistent = 'OK')
         else:
            sweetify.error(request,'an error occured',persistent = ':(')

      
    form = SubscribeForm()
    context = {'form': form}
    return render(request , 'website/index.html',context)