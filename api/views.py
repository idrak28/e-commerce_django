from rest_framework import generics
from .serializer import BookSerializer ,BookStoreSerializer ,AurthorSerializer
from rest_framework.permissions import IsAdminUser
from .models import Book ,BookStore ,Author
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