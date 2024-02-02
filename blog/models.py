from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notice(models.Model):
    topic = models.CharField(max_length=500)
    date = models.DateField()
    desc = models.TextField(max_length=1000)

    def __str__(self):
        return self.topic

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length = 225)
    
    

    

    
    
