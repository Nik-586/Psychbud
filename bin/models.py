from django.db import models

# Create your models here.
class User(models.Model):
    Name= models.CharField(max_length=45)
    MobileNo= models.IntegerField()
    Email = models.EmailField()
    Password=models.CharField(max_length=20)
