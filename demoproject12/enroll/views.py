from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import Stu_Details,EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib import messages

# Create your views here.

## Sign_Up View Function
def Sign_Up(request):
    if request.method=='POST':
        fm=Stu_Details(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Stu_Details()
    
    return render(request,'enroll/signup.html',{'form':fm})

## Login View Function
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
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


## Profile View Function
def User_Profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated')
                fm.save()
        else:
            fm=EditUserProfileForm(instance=request.user)

        return render(request,'enroll/user_profile.html',{'user':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

## Logout View Function
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

## Change_Password View Function
def Change_Password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

