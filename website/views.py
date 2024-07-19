from django.shortcuts import render
from courses.models import Course


def indexview(request):
    video = Course.objects.get(id=3)
    context = {"specvideo":video}
    return render(request,'website/index.html',context)