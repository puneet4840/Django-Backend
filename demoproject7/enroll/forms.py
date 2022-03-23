from django import forms

class Login(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
