from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
# import jwt
import os
from .serializers import UserRegistrationSerializers, CharacterSerilizer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']


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
                    loan_record = Loan_Record.objects.filter(user=user.id)
                    serializer = LoanSerializer(loan_record, many=True)
                    response = {'message': 'User loan Records ', 'result': serializer.data}
                    return Response(response, status=status.HTTP_200_OK)
                except IndexError:
                    response = {'message': f' Hi 👋 {user.username}, you have no loan records yet 😔.'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
