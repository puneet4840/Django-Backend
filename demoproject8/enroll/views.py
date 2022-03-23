from django.shortcuts import render
from . models import User_registration
from . forms import Registration
from django.http import HttpResponseRedirect

# Create your views here.

def register_redirect(request):
    return render(request,'enroll/success.html')

def update(request):
    return render(request,'enroll/update_success.html')

def user_regis(request):
    if request.method=="POST":
        reg_form=Registration(request.POST)
        if reg_form.is_valid():
            name=reg_form.cleaned_data['name']
            email=reg_form.cleaned_data['email']
            password=reg_form.cleaned_data['password']

            db=User_registration(name=name,email=email,password=password)
            db.save()

            return HttpResponseRedirect('/success/')
        
    else:
        reg_form=Registration()

    return render(request,'enroll/registration.html',{'form':reg_form})

def Delete_data(request):
    if request.method=="POST":
        fm=Registration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']

            db=User_registration(id=2)
            db.delete()

    else:
        fm=Registration()
    return render(request,'enroll/registration.html',{'form':fm})

def update_data(request):
    if request.method=="POST":
        r_f=Registration(request.POST)
        if r_f.is_valid():
            nm=r_f.cleaned_data['name']
            em=r_f.cleaned_data['email']
            pw=r_f.cleaned_data['password']

            db=User_registration(id=3,name=nm,email=em,password=pw)
            db.save()

            return HttpResponseRedirect('/update/')
    else:
        r_f=Registration()
    return render(request,'enroll/registration.html',{'form':r_f})

