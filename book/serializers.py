from rest_framework.serializers import ModelSerializer, ListSerializer
from .models import UserBook, BookNote

class UserBookSerializer(ModelSerializer):
    class Meta:
        model = UserBook
        fields = ['book_id', 'title', 'author', 'rating', 'pages', 'start_date', 'finish_date', 'retelling', 'private']
        extra_kwargs = {
            # 'private': {'write_only': True},
            'book_id': {'read_only': False, 'required': False}
        }
    
    def create(self, user, validated_data):
        book = UserBook.objects.create(
            user = user,
            title = validated_data['title'],
            author = validated_data['author'],
            rating = validated_data['rating'],
            pages = validated_data['pages'],
            retelling = validated_data['retelling'],
            start_date = validated_data['start_date'],
            finish_date = validated_data['finish_date'],
            private = validated_data['private']
        )
        book.save()
        return book
    
    def update(self, instance, validated_data):
        if "book_id" in validated_data.keys():
            book = UserBook.objects.filter(book_id=validated_data['book_id']).update(**validated_data)
            book = UserBook.objects.get(book_id=validated_data['book_id'])
            return book
            
        book = self.create(user=instance, validated_data=validated_data)
        return book


class BookNoteListSerializer(ListSerializer):
    def update(self, instance, validated_data):
        result = []
        for item in validated_data:
            if 'note_id' in item.keys():
                note = BookNote.objects.filter(note_id=item['note_id']).update(**item)
                print(note)
                result.append(note)
            else:
                note = BookNote.objects.create(book=instance, **item)
                result.append(note)
        return result 


class BookNoteSerializer(ModelSerializer):
    class Meta:
        model = BookNote
        fields = ('note_id', 'text', 'private')
        list_serializer_class = BookNoteListSerializer 
        extra_kwargs = {
            'private': {'write_only': True},
            'note_id': {'read_only': False, 'required': False}
        }

    # def create(self, validated_data):
    #    print(validated_data)
    #    return None  



        