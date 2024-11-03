from django.urls import path
from .views import get_all_collections, get_collection_books, create_collection

urlpatterns = [
    path('user/<slug:username>', get_all_collections, name='all_collections'),
    path('<slug:collection_uuid>/books', get_collection_books, name='collections_books'),
    path('create', create_collection, name='create_collection'),
]