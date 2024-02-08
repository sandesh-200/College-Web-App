from django.db import models
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
    
class Picture(models.Model):
    user_image = models.ImageField(upload_to="user_images") 

    

    
    
    

    

    
    
