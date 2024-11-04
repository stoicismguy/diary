from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .services import get_user_books, get_book, get_book_notes
from userProfile.services import UserDAL

from .serializers import UserBookSerializer, BookNoteSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_user_books_view(request, username):
    if str(request.user.username) == username:
        books = get_user_books(request.user, private=True)
        return Response(UserBookSerializer(books, many=True).data)
    
    book_owner = UserDAL.get_user_by_username(username)
    books = get_user_books(book_owner)
    return Response(UserBookSerializer(books, many=True).data)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_book_notes_view(request, book_uuid):
    book = get_book(book_uuid)
    if str(request.user.id) == str(book.user.id):
        notes = get_book_notes(book_uuid, private=True)
        print(notes)
        return Response(BookNoteSerializer(notes, many=True).data)
    notes = get_book_notes(book_uuid)
    return Response(BookNoteSerializer(notes, many=True).data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def add_book_view(request):
    serializer = UserBookSerializer(instance=request.user, data=request.data)
    if serializer.is_valid():
        try:
            book = serializer.save()
            return Response(UserBookSerializer(book).data, status=200)
        except:
            return Response({"error": "get an error"}, status=400)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def add_book_note(request, book_uuid): 
    book = get_book(book_uuid)
    print(request.data)
    serializer = BookNoteSerializer(instance=book, data=request.data, many=True)
    if serializer.is_valid():
        notes = serializer.save()
        return Response({"success": "true"}, status=200)
    else:
        return Response(serializer.errors, status=400)
    

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def delete_book(request, uuid):
    book = get_book(uuid)
    if book.user == request.user:
        book.delete()
        return Response(status=204)
    return Response({'detail': "No access to delete it"})

