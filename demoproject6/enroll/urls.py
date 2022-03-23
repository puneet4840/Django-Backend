from django.urls import path
from . import views

urlpatterns=[
    path('registration/', views.user_registration),
    path('login/', views.user_login),
]