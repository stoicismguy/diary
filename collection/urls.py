from django.urls import path
from collection import views

urlpatterns = [
    path('user/<slug:username>', views.get_all_collections, name='all_collections'),
    path('<slug:collection_uuid>/books', views.get_collection_books, name='collections_books'),
    path('create', views.create_collection, name='create_collection'),
    path('<slug:uuid>/delete', views.delete_collection, name='delete_colllection'),
    path('<slug:uuid>/set_privacy', views.change_collection_privacy, name='change_privacy'),
    path('<slug:uuid>/add_book', views.add_book_to_collection, name='add_book'),
    path('<slug:uuid>', views.collection_info, name='collection_info'),
]