from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view("GET")
@authentication_classes(TokenAuthentication)
def get_all_collections(request, username):
    return Response({"test": request.user.username})