from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import datetime

from .models import Student


# Create your views here.

def homeView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('visitor'))
     
    return render(request, 'index.html', {'student_information':Student.objects.all()})


def notAuthenticUser(request):
    return render(request, 'display.html')


def detailsView(request, pk):
    dateInfo = str(datetime.datetime.today().day) + '/' + str(datetime.datetime.today().month) + '/' + str(datetime.datetime.today().year)
    return render(request, 'details.html', {'dateInfo':dateInfo})