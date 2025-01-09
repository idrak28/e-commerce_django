from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class BookStore(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
   
class Author(models.Model):
    name=models.CharField(max_length=50)  
    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name='book_list', blank=True,null=True )
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    store_name = models.ForeignKey(BookStore, on_delete=models.CASCADE ,blank=True,null=True , related_name='book_list')
    
    @property
    def in_stock(self):
        return self >0
    
    def __str__(self):
        return self.name
