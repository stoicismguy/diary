from .models import UserBook, BookNote
from django.core.exceptions import ValidationError


def get_user_books(user, private=False):
    if not private:
        books = UserBook.objects.filter(user=user, private=private)
        return books
    books = UserBook.objects.filter(user=user)
    return books


def get_book(book_uuid):
    book = UserBook.objects.get(book_id=book_uuid)
    return book


def get_book_notes(book_uuid, private=False):
    book = get_book(book_uuid)
    if not private:
        notes = BookNote.objects.filter(book=book, private=private)
        return notes
    notes = BookNote.objects.filter(book=book)
    return notes





        
    
    
