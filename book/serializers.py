from rest_framework.serializers import ModelSerializer
from .models import UserBook, BookNote

class UserBookSerializer(ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['title', 'author', 'rating', 'start_date', 'finish_date', 'retelling']



class BookNoteSerializer(ModelSerializer):
    class Meta:
        model = BookNote
        fields = ['text']