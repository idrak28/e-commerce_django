
from django.urls import path

from .views import (AurthorAPIView, BookDetailAPIView, BookListCreateAPIView,
                    BookstoreAPIView, OrderDetailAPIView, OrderListAPIView,
                    UserOrderListAPIView)

urlpatterns = [
    path('book/', BookListCreateAPIView.as_view()) ,
    path('author/', AurthorAPIView.as_view()) ,
    path('book/<int:product_id>/',BookDetailAPIView.as_view()) ,
    path('orders/<int:order_id>/',OrderDetailAPIView.as_view()) ,
    path('bookstore/',BookstoreAPIView.as_view()) ,
    path('orders/',OrderListAPIView.as_view()) , 
    path('user-orders/',UserOrderListAPIView.as_view() , name='user-orders' ) ,
]
