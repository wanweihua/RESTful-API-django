# --*-- coding: utf-8 --*--
from django.contrib.auth.models import User
from rest_framework import generics
from app.permissions import IsAuthenticatedOrCreate
from app.serializers.serializer_signup import SignSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignSerializer
    permission_classes = (IsAuthenticatedOrCreate,)