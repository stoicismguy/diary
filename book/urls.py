from django.urls import path
from book import views

urlpatterns = [
    path('search/websearch/', views.website_search, name='search'),
    path('user/<slug:username>/', views.get_user_books_view, name='user_books'),
    path('<slug:book_uuid>/notes/', views.get_book_notes_view, name='book_notes'),
    path('<slug:uuid>', views.get_book_info, name='book_info'),
    path('<slug:uuid>/collections', views.get_book_collections, name='get_book_collections'),
    path('<slug:book_uuid>/notes/add', views.add_book_note, name='add_book_note'),
    path('<slug:uuid>/delete', views.delete_book, name='delete_book'),
    path('create_or_update/', views.add_book_view, name='add_book_view'),
    path('get_two_last/', views.get_two_last, name='get_two_last'),
]