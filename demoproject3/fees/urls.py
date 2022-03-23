from django.urls import path
from . import views

urlpatterns=[
    path('feesdj/',views.course_fee,name='fees_page')
]