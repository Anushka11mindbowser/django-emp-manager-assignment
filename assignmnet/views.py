from .serializers import EmployeeSerializer, RegisterEmployeeSerializer, LoginEmployeeSerializer
from .models import EmployeeUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from rest_framework.generics import (GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView)

class UserDetailsAPI(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        user = EmployeeUser.objects.get(id=request.user.id)
        serializer = EmployeeSerializer(user)
        return Response(serializer.data)

class RegisterUser(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    serializer_class = RegisterEmployeeSerializer

class LoginUser(GenericAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LoginEmployeeSerializer

class RegisterEmployee(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class =