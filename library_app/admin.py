
from django.contrib import admin
from .models import Genre, Book, User,Transactions

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page=10

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'publication_year', 'copies_available', 'total_copies', 'genre',)
    search_fields = ('title', 'author', 'genre__name') 
    list_filter=('title',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address',)
    list_filter=('name',)
    list_per_page=10

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'book', 'borrow_date', 'due_date', 'return_date', 'status', 'is_returned','genre',)
    search_fields = ('user__name', 'book__title', 'genre',)
    list_filter = ('is_returned',)
    list_per_page = 10
