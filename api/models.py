import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


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


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending' 
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
        DELEVERIED = 'Deleveried'
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default = StatusChoices.PENDING )
    products = models.ManyToManyField(Book, through="OrderItem" , related_name='orders')
    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                               on_delete=models.CASCADE , 
                               related_name='items' ) # to match nasted serializer 
    product = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    @property
    def item_subtotal(self):
         return self.product.price * self.quantity
     
    def __str__(self):
         return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"
     
     