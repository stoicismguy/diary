from django.db import models
from userProfile.models import User
import uuid
from django.utils import timezone


# Create your models here.

class UserBook(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    rating = models.FloatField()
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)
    retelling = models.TextField()
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username}, {self.title}'


class BookNote(models.Model):
    note_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(UserBook, on_delete=models.CASCADE)
    text = models.TextField()
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.book.user.username} {self.book.title}'
