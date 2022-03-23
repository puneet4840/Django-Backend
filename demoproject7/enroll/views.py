from django.shortcuts import render
from . forms import Login
from django.http import HttpResponseRedirect 

# Create your views here.

def success_login(request):
    return render(request,'enroll/success_login.html')

def stu_login(request):
    if request.method=="POST":
        fm=Login(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            password=fm.cleaned_data['password']
            print(name)
            print(password)

            return HttpResponseRedirect('/success/')

    else:
        fm=Login()

    return render(request,'enroll/login.html',{'form':fm})