from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
# import jwt
import os
from .serializers import UserRegistrationSerializers
from rest_framework.authentication import TokenAuthentication
from decouple import config


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']

    def list(self, request, version="v1", *args, **kwargs):
        if version in self.versions:
            if request.user:
                try:
                    user = request.user
                    ACCESS_KEY = config('API_ACCESS_KEY')
                    response = requests.get(
                        'https://the-one-api.dev/v2/character',  auth=BearerAuth(ACCESS_KEY))
                    # print(response.json())
                    response = {
                        'message': response.json()}
                    return Response(response, status=status.HTTP_200_OK)
                except IndexError:
                    response = {
                        'message': f' Hi 👋 {user.username}, some errors occured 😔.'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                response = {'message': 'API version not identified!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
