from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(15)
def home(request):
    return render(request,'enroll/home.html')

@cache_page(10)
def contact(request):
    return render(request,'enroll/contact.html')