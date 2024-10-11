from rest_framework.serializers import ModelSerializer, Serializer, CharField
from .models import User

from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, valdiated_data):
        print(valdiated_data)
        user = User.objects.create(
            username = valdiated_data['username'],
            email = valdiated_data['email'],
            first_name = valdiated_data['first_name'],
            last_name = valdiated_data['last_name'],
        )
        user.set_password(valdiated_data['password'])
        user.save()
        return user



class IssueTokenRequestSerializer(Serializer):
    model = User
    username = CharField(required=True)
    password = CharField(required=True)


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
