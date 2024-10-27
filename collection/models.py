from django.db import models
from book.models import UserBook
from userProfile.models import User
# Create your models here.


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    books = models.ForeignKey(UserBook, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"