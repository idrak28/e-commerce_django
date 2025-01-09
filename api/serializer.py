from rest_framework import serializers
from .models import Book , BookStore , Author

class BookSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Book 
        fields= (
            'name' ,
            'author' ,
            'price' ,
            'stock',
            'image' ,
            'store_name'
            
        )
      
class BookStoreSerializer(serializers.ModelSerializer):
    book_list=BookSerializer(many=True)
    class Meta :
        model = BookStore
        fields =(
            'name' ,
            'description' ,
           'book_list'
        )
class AurthorSerializer(serializers.ModelSerializer):
    book_list=BookSerializer(many=True,read_only=True)
    class Meta :
        model = Author
        fields =(
            'name' ,
           'book_list'
        )
