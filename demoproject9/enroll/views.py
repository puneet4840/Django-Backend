from django.shortcuts import render
from .forms import Sign_up_form

# Create your views here.

def sign_up(request):
    if request.method=="POST":
        fm=Sign_up_form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Sign_up_form()

    return render(request,'enroll/sign_up.html',{'form':fm})