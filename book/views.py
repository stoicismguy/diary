from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .services import get_user_books
from userProfile.services import UserDAL

from .serializers import UserBookSerializer



@api_view()
@authentication_classes([TokenAuthentication])
def get_user_books_view(request, user_uuid):
    if str(request.user.id) == str(user_uuid):
        books = get_user_books(request.user, private=True)
        return Response({"books": UserBookSerializer(books, many=True).data})
    book_owner = UserDAL.get_user_by_uuid(user_uuid)
    books = get_user_books(book_owner)
    return Response({"books": UserBookSerializer(books, many=True).data})