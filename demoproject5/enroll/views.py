from django.shortcuts import render
from enroll.models import Student
from enroll.forms import StudentRegistration
# Create your views here.

def student_info(request):
    stud=Student.objects.all()
    form_obj=StudentRegistration()
    return render(request,'enroll/studetails.html',{'stu':stud,'form':form_obj})