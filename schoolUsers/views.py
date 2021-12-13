from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import auth

from .models import UserRegistion

# Create your views here.
def SignIn(request):
    error_message = str()
    if request.POST or None:
        username_user = request.POST.get("username")
        password_user = request.POST.get("password")
        # user = User.objects.create_user(username, password)
        USER_AUTHENTICATION = auth.authenticate(username=username_user, password=password_user)
        # if you found the user in the database
        if USER_AUTHENTICATION:
            login(request, USER_AUTHENTICATION)
            return redirect('/')
        else:
            # Else return it with an alert 
            error_message = "YOU ARE NOT REGISTERED!"
        


    return render(request, 'USER/login.html', {'error': error_message})


def SignUp(request):
    error_message = str

    
    if request.method == "POST":
        DATA = request.POST.get
        Fname = DATA('fname')
        Sname = DATA('sname')
        insituite = DATA('insitution') 
        city = DATA('city')
        state = DATA('state')
        zipCode = DATA('zip')
        phoneNumber = DATA('phone_number')
        email = DATA('email')
        adhaar = DATA('adhaar')
        role = DATA('role')
        schoolCode = DATA('schoolCode')
        password = DATA('password')

        if role == 'pri':
            x = True
        else:
            x = False

        print(state, email)
        
        # if UserRegistion.objects.filter(insitution=insituite):
        #     error_message = "Insituition already registered looks like your insituition is already registered, forgotten password?"
        #     return render(request, 'USER/signUp.html', {'error':error_message})
        # else:
        #     user = UserRegistion.objects.create(Fname=Fname, Sname=Sname, insitution=insituite, city=city, state=state, zipcode=zipCode, phone_number=phoneNumber,email=email, adhaar=adhaar, role=x, schoolCode=schoolCode, password=password)
        #     new_user = ''

        UserRegistion.objects.create(Fname=Fname, Sname=Sname, insitution=insituite, city=city, state=state, zipcode=zipCode, phone_number=phoneNumber,email=email, adhaar=adhaar, role=x, schoolCode=schoolCode, password=password)
        new_user = User.objects.create_user(username=Fname, first_name=Fname, last_name=Fname, email=email, password=password, is_staff=x)
        login(request, new_user)
        return redirect('/')

    return render(request, 'USER/signUp.html')


