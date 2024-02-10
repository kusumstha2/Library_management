from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Genre, Book, User, Transactions
from rest_framework import filters
from django_filters import rest_framework as filter
from .permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class GenreViewset(viewsets.ModelViewSet):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields =('name',)
    search_fields=('name',)
    
    
    
    

class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer 
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,) 
    search_fields=('name','email','address',)  
    permission_classes=(IsAuthenticatedOrReadOnly,)
    
class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields =('title','genre',)
    search_field=('title',)  

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset=Transactions.objects.all()
    serializer_class=TransactionsSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,) 
    search_field=('user',)    

"""class RecipeViewset(viewsets.ModelViewSet):
    queryset=Recipe.objects.select_related('category').all()
    serializer_class=RecipeSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend,)
    filterset_class= RecipeFilter
    search_fields=('name',)
    permission_classes=(IsAuthenticatedOrReadOnly,)"""