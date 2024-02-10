from django.db import models

# Create your models here.

# Create your models here.
from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self)->str:
        return self.name  

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_year = models.DateField()
    copies_available = models.IntegerField()
    total_copies = models.IntegerField()
    genre = models.ForeignKey(Genre,null=True,blank=True, on_delete=models.PROTECT )

    def __str__(self) ->str:
        return f"{self.title} by {self.author} and genre:{self.genre.name}"

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self)->str:
        return self.name

class Transactions(models.Model):
    DONE_CHOICE = 'D'
    PENDING_CHOICE = 'P'
    RETURNED_STATUS = [
        (DONE_CHOICE, 'DONE'),
        (PENDING_CHOICE, 'PENDING'),
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=RETURNED_STATUS, default=PENDING_CHOICE)
    is_returned = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Transaction ID: {self.id}, User: {self.user.name}, Book: {self.book.title}, Genre: {self.genre.name}"    

