from rest_framework import serializers
from .models import *
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'name',)
        model=Genre
    # id=serializers.IntegerField()
    # name=serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'name',
            'email',
            'phone',
            'address',
            
        )    
        model=User
        

class BookSerializer(serializers.ModelSerializer) :
    class Meta:
        fields=(
            
            'title',
            'author',
            'publication_year',
            'copies_available',
            'total_copies',
            'genre',
        )  
        model=Book  
        

class TransactionsSerializer(serializers.ModelSerializer) :
    book=serializers.StringRelatedField()
    book_id=serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source="book")
    
    user=serializers.StringRelatedField()
    user_id=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="user")
    
    genre=serializers.StringRelatedField()
    genre_id=serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source="genre")
    
    class Meta:
        fields=(
            'user_id',
            'user',
            'book_id',
            'book',
            'borrow_date',
            'due_date',
            'return_date',
            'status',
            'is_returned',
            'genre_id',
            'genre',
            
        )  
        model=Transactions   