from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ProfileView(APIView):
    def get(self, request):
        return Response({"get": "profile"})
    
    def post(self, request):
        return Response({"post": "profile"})