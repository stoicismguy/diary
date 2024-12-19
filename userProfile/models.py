from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bio = models.TextField(null=True, max_length=500)

    def __str__(self) -> str:
        return f'{self.username} {self.id}'
    

    