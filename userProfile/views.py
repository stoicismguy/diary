from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


from .serializers import UserSerializer, IssueTokenRequestSerializer, TokenSerializer

from .services import get_user_profile

# Create your views here.


class ProfileView(APIView):
    def get(self, request):
        # profile = get_user_profile(request.user)
        return Response({"get": "profile"})
    
    def post(self, request):
        return Response({"post": "profile"})
    

@api_view()
@authentication_classes([TokenAuthentication])
def user(request):
    return Response({
        'data': UserSerializer(request.user).data
    })


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
        