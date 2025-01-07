
from django.urls import path 
from .views import BookListCreateAPIView 
urlpatterns = [
    path('book/', BookListCreateAPIView.as_view()) ,
      
]
