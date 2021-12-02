from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def homeView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('visitor'))
    return render(request, 'index.html')

def notAuthenticUser(request):
    return render(request, 'display.html')