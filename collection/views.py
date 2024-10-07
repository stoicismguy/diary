from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ProfileView(APIView):
    def get(request):
        return Response({"get": "profile"})
    
    def post(request):
        return Response({"post": "profile"})