from django.shortcuts import render
from enroll.forms import Stu_form

# Create your views here.

def stu_details(request):
    if request.method=='POST':
        fm=Stu_form(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            ct=fm.cleaned_data['city']
            pw=fm.cleaned_data['password']
            print(nm)
            print(ct)
            print(pw)
        
    else:
        fm=Stu_form()
    return render(request,'enroll/details.html',{'form':fm})