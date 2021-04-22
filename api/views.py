from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
# import jwt
import os
from .serializers import UserRegistrationSerializers
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']


class CharacterViewSet(viewsets.ModelViewSet):
