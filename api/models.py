from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class Book(models.Model):
    name = models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    
    
    @property
    def in_stock(self):
        return self >0
    
    def __str__(self):
        return self.name
     