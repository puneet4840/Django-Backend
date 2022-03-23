from django import forms
from enroll.models import Stu

class Stu_form(forms.ModelForm):
    class Meta:
        model=Stu
        fields=['name','city','password']
        labels={'name':'Enter Name','city':'Enter City','password':'Enter Password'}
        widgets={'password':forms.PasswordInput}