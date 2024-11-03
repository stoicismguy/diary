from book.models import UserBook
from .models import Collection
from userProfile.services import UserDAL


def get_user_collections(username, private=False):
    user = UserDAL.get_user_by_username(username)
    if not private:
        result = Collection.objects.filter(user=user, private=private)
        return result
    result = Collection.objects.filter(user=user)
    return result


def get_book_in_collection(collection_uuid: str)-> tuple:
    collection = Collection.objects.get(uuid=collection_uuid) 
    return (collection, collection.get_books())