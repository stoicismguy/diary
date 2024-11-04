from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .services import get_user_collections, get_book_in_collection, get_collection_via_uuid
from .serializers import CollectionSerializer
from book.serializers import UserBookSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_all_collections(request, username):
    if request.user.username == username:
        collections = get_user_collections(username, private=True)
    else:
        collections = get_user_collections(username)
    return Response(CollectionSerializer(collections, many=True).data, status=200)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_collection_books(request, collection_uuid):
    collection, books = get_book_in_collection(collection_uuid)
    print(books)
    if collection.private and collection.user != request.user:
        return Response({"detail": "Requested collection is private"}, status=403) 
    return Response(UserBookSerializer(books, many=True).data, status=200)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def create_collection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        try:
            collection = serializer.create(user=request.user, validated_data=serializer.validated_data)
            return Response(CollectionSerializer(collection).data, status=201)
        except:
            return Response({"detail": "got an unexpected error"}, status=400)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def delete_collection(request, uuid):
    collection = get_collection_via_uuid(uuid)
    if request.user == collection.user:
        collection.delete()
        return Response(status=204)
    return Response({'detail': 'No access to delete it'}, status=403)  




