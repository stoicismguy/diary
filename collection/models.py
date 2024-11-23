from django.db import models
from book.models import UserBook
from userProfile.models import User
import uuid


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=120)
    private = models.BooleanField(default=False)
    books = models.ManyToManyField(UserBook, related_name="collections")


    def __str__(self) -> str:
        return f"{self.user.username}:{self.title}"
    
    def get_books(self):
        books = self.books.all()
        return books

    def get_book_count(self):
        return self.books.all().count()