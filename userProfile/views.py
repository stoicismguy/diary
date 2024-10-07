from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_user_profile

# Create your views here.


class ProfileView(APIView):
    def get(self, request):
        # profile = get_user_profile(request.user)
        return Response({"get": "profile"})
    
    def post(self, request):
        return Response({"post": "profile"})
    
