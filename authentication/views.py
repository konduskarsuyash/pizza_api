from django.shortcuts import render

from rest_framework import generics,status
from rest_framework.response import Response

from .models import User
from .serializers import UserCreationSerializer

from drf_yasg.utils import swagger_auto_schema

class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello auth"},status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="Create a new user")
    def post(self, request):
        data = request.data
    
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)