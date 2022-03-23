from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course_fee(request):
    fee_dict={
        'course_name':'Django',
        'fees':'Rs/5000'
    }
    return render(request,'fees/feesone.html',fee_dict)