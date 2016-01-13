# --*-- coding: utf-8 --*--
from oauth_provider.backends import User
from rest_framework import serializers


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        filed = ('username', 'password')
        write_only_filed = ('password')
