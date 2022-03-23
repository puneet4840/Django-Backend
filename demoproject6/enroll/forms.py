from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    password=forms.CharField()

class StudentLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
