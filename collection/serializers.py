from book.models import UserBook
from .models import Collection
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CollectionSerializer(ModelSerializer):
    book_count = SerializerMethodField('get_book_count')

    def create(self, user, validated_data):
        collection = Collection.objects.create(
            user=user,
            title=validated_data['title'],
            private=validated_data['private']
        )
        collection.save()
        return collection

    def get_book_count(self, collection):
        return collection.get_book_count()


    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'private', 'book_count']
        extra_kwargs = {
            'uuid': {'read_only': True},
            'private': {'write_only': True},
            'book_count': {'read_only': True}
        }


