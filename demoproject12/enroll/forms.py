from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class Stu_Details(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}


class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','is_staff','is_active','date_joined','last_login']
        labels={'email':'Email'}