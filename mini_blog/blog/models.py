
from turtle import title

from django.db import models

# Create your models here.
class Blog_Post(models.Model):
    title = models.CharField(max_length=900)
    desc = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name 
