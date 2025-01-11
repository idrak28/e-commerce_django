# Create your views here.
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Author, Book, BookStore, Order
from .serializer import (AurthorSerializer, BookSerializer,
                         BookStoreSerializer, OrderItemSerializer,
                         OrderSerializer)


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
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    
    serializer_class = BookSerializer
    lookup_url_kwarg = 'product_id'
    def get_permissions(self):
        self.permission_classes =[AllowAny]
        if self.request.method in ['PUT' , 'PATCH' , 'DELETE']:
            self.permission_classes =[IsAdminUser]
        return super().get_permissions() 
    
class BookstoreAPIView(generics.ListAPIView):
    
    queryset=BookStore.objects.all()
    serializer_class =BookStoreSerializer
class AurthorAPIView(generics.ListAPIView):
    
    queryset=Author.objects.all()
    serializer_class = AurthorSerializer
    
class OrderListAPIView(generics.ListAPIView):
    
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    def get_permissions(self):
       
        self.permission_classes =[IsAdminUser]
        return super().get_permissions() 
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'
    def get_permissions(self):
        self.permission_classes =[AllowAny]
        if self.request.method in ['PUT' , 'PATCH' , 'DELETE']:
            self.permission_classes =[IsAdminUser]
        return super().get_permissions() 
    
    
class UserOrderListAPIView(generics.ListAPIView):
    
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
   
        qs=super().get_queryset()
            
        
        return qs.filter(user=self.request.user)