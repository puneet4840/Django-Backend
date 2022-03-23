from django.contrib import admin
from . models import User_registration

# Register your models here.

class Student_admin(admin.ModelAdmin):
    list_display=('id','name','email','password')

admin.site.register(User_registration,Student_admin)