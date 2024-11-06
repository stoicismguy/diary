from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, IssueTokenRequestSerializer, TokenSerializer, RegisterSerializer

from .services import UserDAL


@api_view()
@authentication_classes([TokenAuthentication])
def user_info(request, username):
    user = UserDAL.get_user_by_username(username)
    stat = UserDAL.get_stat(user)
    return Response({"user": UserSerializer(user).data, "statistics": stat})

    
@api_view()
@authentication_classes([TokenAuthentication])
def user(request):
    return Response(UserSerializer(request.user).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def issue_token(request):
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        auth_user = authenticate(**serializer.validated_data)
        try:
            token = Token.objects.get(user=auth_user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=auth_user)
        return Response(TokenSerializer(token).data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])        
def user_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(serializer.validated_data)
        if user:
            token = Token.objects.create(user=user)
            return Response(TokenSerializer(token).data)
    return Response(serializer.errors, status=400)