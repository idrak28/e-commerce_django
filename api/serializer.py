from rest_framework import serializers

from .models import Author, Book, BookStore, Order, OrderItem


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
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(max_digits=10 ,
                                             decimal_places=2,
                                             source='product.price')
    class Meta :
        model = OrderItem
        fields = ('product_name','product_price', 'quantity' , 'item_subtotal')
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True , read_only =True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
        
    class Meta :
         model =Order
         fields =  ('order_id' , 
                    'created_at',  
                    'user' , 
                    'status' , 
                    'items' , 
                    'total_price' , )