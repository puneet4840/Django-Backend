from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse('Welcome to the Django World !!!')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1>Learn Python</h1>')

def learn_math(request):
    return HttpResponse(10+10)