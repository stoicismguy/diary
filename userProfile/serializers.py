from rest_framework.serializers import ModelSerializer, Serializer, CharField
from .models import User

from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
        

class IssueTokenRequestSerializer(Serializer):
    model = User
    username = CharField(required=True)
    password = CharField(required=True)


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
