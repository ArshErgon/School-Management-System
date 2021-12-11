from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

import datetime

from schoolUsers.models import UserRegistion

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
    for i in Student.objects.filter(pk=pk):
        pass
    return render(request, 'details.html', {'dateInfo':dateInfo, 'student':i})

    
def addStudent(request):
    username = request.user.username
    school = UserRegistion.objects.filter(username=username)
    for i in school:
        pass

    if request.method == 'POST':
        add_info = request.POST.get
        insitution = i.insitution
        fName = add_info("fname")
        sName = add_info("sname")
        student_code = add_info("sCode")
        FatherName = add_info("fatherName")
        MotherName = add_info("motherName")
        fee = add_info("fee")
        DOB = add_info("dob")
        presentClass = add_info("presentClass")
        address = add_info("address")
        state = add_info("state")
        city = add_info("city")
        phoneNumber = add_info("phoneNumber")
        adhaar = add_info("adhaar")
        religion = add_info("religion")
        caste = add_info("caste")
        category = add_info("category")
        rte_student = add_info("rte")
        relatives_in_school = add_info("relatives")
        email = add_info("emailfield")
        # Student.objects.create(insitution=insitution, student_code=student_code, fName = fName, sName = sName, fatherName = FatherName, motherName = MotherName, fee = fee, DOB = DOB,  student_present_class=presentClass, address = address, phoneNumber = phoneNumber, email=email, adhaar= adhaar, religion=religion, caste=caste, category=category, rte_student=rte_student, relatives_in_school=relatives_in_school, state=state, city=city)
        return redirect('/')        
    return render(request, 'student/addingstudent.html')