from django.urls import path
from collection import views

urlpatterns = [
    path('user/<slug:username>', views.get_all_collections, name='all_collections'),
    path('<slug:collection_uuid>/books', views.get_collection_books, name='collections_books'),
    path('create', views.create_collection, name='create_collection'),
    path('<slug:uuid>/delete', views.delete_collection, name='delete_colllection'),
]