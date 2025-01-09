
from django.urls import path 
from .views import BookListCreateAPIView ,BookstoreAPIView ,BookDetailAPIView ,AurthorAPIView
urlpatterns = [
    path('book/', BookListCreateAPIView.as_view()) ,
    path('author/', AurthorAPIView.as_view()) ,
    path('book/<int:product_id>/',BookDetailAPIView.as_view()) ,
    path('bookstore/',BookstoreAPIView.as_view()) ,
]
