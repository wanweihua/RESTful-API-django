# --*-- coding: utf-8 --*--
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from app.permissions import IsAuthenticatedOrCreate
from app.serializers.serializer_auth import SignUpSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


    def pre_save(self, object):
        object.owner = self.request.user
