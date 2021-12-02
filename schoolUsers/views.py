from django.shortcuts import render
from django.contrib.auth.models import User

from .models import UserRegistion

# Create your views here.
def SignIn(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        # user = User.objects.create_user(username, password)
        
    return render(request, 'USER/login.html')


def SignUp(request):
    error_message = str

    
    if request.method == "POST" or "post":
        DATA = request.POST.get
        Fname = DATA('fname')
        Sname = DATA('sname')
        insituite = DATA('insitiute') 
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
        
        # if UserRegistion.objects.filter(insitution=insituite):
        if x:
        # Insituition already Exists
            error_message = "Insituition already registered looks like your insituition is already registered, forgotten password?"
            print("error_message")
            return render(request, 'USER/signUp.html', {'error':error_message})
        else:
            pass


    return render(request, 'USER/signUp.html')