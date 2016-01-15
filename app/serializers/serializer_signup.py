# --*-- coding: utf-8 --*--
from django.contrib.auth.models import User

from rest_framework import serializers


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        filed = ('username', 'password')
        write_only_filed = ('password')
