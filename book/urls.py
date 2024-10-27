from django.urls import path
# from .views import get_user_books_view, get_book_notes_view, add_book_view
from book import views

urlpatterns = [
    path('user/<slug:username>/', views.get_user_books_view, name='user_books'),
    path('<slug:book_uuid>/notes/', views.get_book_notes_view, name='book_notes'),
    path('<slug:book_uuid>/notes/add', views.add_book_note, name='add_book_note'),
    path('create_or_update/', views.add_book_view, name='add_book_view'),
]