from rest_framework import generics
from .serializer import BookSerializer 
from rest_framework.permissions import IsAdminUser
from .models import Book 
from rest_framework.permissions import IsAuthenticated ,IsAdminUser ,AllowAny
# Create your views here.
from rest_framework import filters

class BookListCreateAPIView(generics.ListCreateAPIView):
    
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    
    filter_backends =[
       # DjangoFilterBackend, # django filter.py
        filters.SearchFilter,   #?search=coffe
        filters.OrderingFilter ]
    ordering_fileds = [ 'name' , 'price']
    search_fields = ['name' , 'description']
    
