from django.shortcuts import render
from . forms import StudentRegistration,StudentLogin

# Create your views here.

def user_registration(request):
    stureg_form=StudentRegistration
    return render(request,'enroll/registration.html',{'reg':stureg_form})

def user_login(request):
    stulog=StudentLogin
    return render(request,'enroll/login.html',{'login':stulog})