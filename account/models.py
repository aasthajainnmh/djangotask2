from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
class Post(models.Model):
    CATEGORY_CHOICES=(
        ('Mental Health','Mental Health'),
        ('Heart Diseases','Heart Diseases'),
        ('Covid19','Covid19'),
        ('Immunization','Immunization'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    summary=models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
