from django.urls import path
from rest_framework import routers
from .views import *
router=routers.SimpleRouter()
router.register(r'genre',GenreViewset,basename='genre')
router.register(r'user',UserViewset,basename='user')
router.register(r'book',BookViewSet,basename='book')
router.register(r'transactions',TransactionsViewSet,basename='transactions')
#router.register(r'transactions',TransactionsViewset)

urlpatterns =router.urls+ [
    
]