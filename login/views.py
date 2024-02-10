from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework.views import APIView
class LoginAPIView(APIView):
    
    def  post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username == None and password== None:
            raise serializers.ValidationError(
                {
                    "details":"User and Password Field are required"
                }
            )
        user=authenticate(username=username,password=password)
        if user:
            token,_= Token.objects.get_or_create(user=user)
                 
            
            return Response({
                    'token':token.key,
                    'user':user.username
                })
        return Response({
                "details":"User or password is invalid"
            },status=status.HTTP_401_UNAUTHORIZED)
                