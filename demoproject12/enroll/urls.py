from django.urls import path
from enroll import views

urlpatterns=[
    path('signup/',views.Sign_Up,name='signupform'),
    path('login/',views.Login,name="loginform"),
    path('profile/',views.User_Profile,name="user_profile"),
    path('logout',views.Logout,name="logout"),
    path('changepass/',views.Change_Password,name='changepassform')
]