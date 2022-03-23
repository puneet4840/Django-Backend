from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Sign_up_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}