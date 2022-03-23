from django.shortcuts import render

# Create your views here.

def homepage(request):
    home_dict={
        'name':'Puneet'
    }
    return render(request,'homepage/homepage.html',home_dict)

def aboutpage(request):
    return render(request,'homepage/aboutpage.html')