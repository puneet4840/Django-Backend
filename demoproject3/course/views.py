from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    dj_dict={
        'course_name':'Django',
        'du':'4 weeks',
    }
    return render(request,'course/courseone.html',dj_dict)