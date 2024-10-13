from django.urls import path
from .views import get_user_books_view

urlpatterns = [
    path('user_books/<slug:user_uuid>', get_user_books_view, name='user_books')
]