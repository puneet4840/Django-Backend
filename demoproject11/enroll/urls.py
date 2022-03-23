from django.urls import path
from enroll import views

urlpatterns=[
    path('signup/',views.Sign_Up,name='user_signup'),
    path('login/',views.Login,name='user_login'),
    path('profile/',views.new_page,name='profile'),
    path('logout/',views.user_Logout,name='logout_page'),
]