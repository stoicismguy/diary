from django.db import models
from book.models import UserBook
from userProfile.models import User
# Create your models here.


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    private = models.BooleanField(default=False)
    books = models.ManyToManyField(UserBook)


    def __str__(self) -> str:
        return f"{self.user.username}:{self.title}"
    
    def get_books(self):
        books = self.books.all()
        return books

