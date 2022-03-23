from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.stu_login),
    path('success/',views.success_login),
]