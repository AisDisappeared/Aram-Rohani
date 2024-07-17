from django.shortcuts import render



def indexview(request):
    return render(request,'website/index.html')