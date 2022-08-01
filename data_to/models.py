from django.db import models

# Create your models here.
class Information(models.Model):
    name= models.CharField(max_length=30)
    age= models.TextField()
    city= models.CharField(max_length=30)