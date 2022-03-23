from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    password=models.CharField(max_length=20)