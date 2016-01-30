# --*-- coding: utf-8 --*--
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.permissions import IsAuthenticatedOrCreate
from app.serializers.serializer_auth import SignUpSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

    def pre_save(self, object):
        object.owner = self.request.user
