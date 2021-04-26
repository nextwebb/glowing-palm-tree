from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
from rest_framework.decorators import action
# import jwt
import os
from .serializers import UserRegistrationSerializers
from rest_framework.authentication import TokenAuthentication
from decouple import config


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers  # used by serializers output

    # this option is used to authenticate a user, thus django can identify the token and its
    authentication_classes = (TokenAuthentication,)
    # owner
    permission_classes = (AllowAny,)
    versions = ['v1']

# If you are using requests module, an alternative option is to write an auth class,


# which allows you to use the same auth argument just like basic auth, and may help you in certain situations.

# and then can you send requests like this

# response = requests.get('https://www.example.com/', auth=BearerAuth('3pVzwec1Gs1m'))

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']

    def list(self, request, version="v1", *args, **kwargs):
        if version in self.versions:
            if request.user:
                try:
                    user = request.user
                    # access the key from the environmental variable
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

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

#
    @action(detail=True, methods=['GET'])
    def quotes(self, request, version="v1", pk=None):
        if version in self.versions:
            if request.user:
                try:
                    print(pk)
                    user = request.user
                    ACCESS_KEY = config('API_ACCESS_KEY')
                    # this api seems to take a while and sometimes timesouts
                    # needs to be optimized
                    response = requests.get(
                        f'https://the-one-api.dev/v2/character/{pk}/quote',  auth=BearerAuth(ACCESS_KEY))
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

            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class QouteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']


class FavouritesViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']
