from django.contrib import admin

from api.models import Author, Book, BookStore, Order, OrderItem, User

# Register your models her


admin.site.register(User)

class BookOffer(admin.ModelAdmin):
    
    list_display=['name','price']
    list_editable =['price']
    
    actions=('book_offer','book_main_price')
    
    @admin.action(description="Discount Price")
    def book_offer(self,request,queryset):
        for obj in queryset:
            obj.price = float(obj.price) * 95/100
            obj.save()
            
    @admin.action(description="Orginal Price")
    def book_main_price(self,request,queryset):
        for obj in queryset:
            obj.price = float(obj.price) * 100/95
            obj.save()
   # @admin.action(description="Make select properties available")
   # def make_available(self, request, queryset):
    #    queryset.update(availability=True)       
            
admin.site.register(Book,BookOffer)
admin.site.register(BookStore)
admin.site.register(Author)
class OrderItemInline(admin.TabularInline):
    model = OrderItem 

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        
        OrderItemInline
    ]
admin.site.register(Order,OrderAdmin)
