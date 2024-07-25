from django.http import HttpResponseRedirect
from django.urls import reverse




# def change_mode(request):
#     if 'is_dark_mode' in request.session:
#         request.session['is_dark_mode'] = not request.session['is_dark_mode'] 
#     else:
#         request.session['is_dark_mode'] = True
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def change_mode(request):
    # Toggle the dark mode preference
    if request.session.get('is_dark_mode', False):
        request.session['is_dark_mode'] = False
    else:
        request.session['is_dark_mode'] = True
    
    # Redirect back to the referring page or a default page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('website:home')))