from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from enroll.forms import sign_up
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

## Sign_up View Function
def Sign_Up(request):
    if request.method=="POST":
        fm=sign_up(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=sign_up()

    return render(request,'enroll/sign_up_form.html',{'form':fm})

## Login View function
def Login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    messages.success(request,'Successfully Login')
                    return HttpResponseRedirect('/profile/')

        else:
            fm=AuthenticationForm()
    
        return render(request,'enroll/login_form.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    

## Redirect View function
def new_page(request):
    if request.user.is_authenticated:
        return render(request,'enroll/new_page.html',{'user':request.user})
    else:
        return HttpResponseRedirect('/login/')


## Logout View function
def user_Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')