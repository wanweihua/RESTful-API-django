# --*-- coding: utf-8 --*--
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        write_only_fields = ('password')
        read_only_field = ('id')

        def create(self, validated_data):
            """
            passwordをハッシュ化して登録
            :param validated_data:
            :return:
            """

            password = validated_data.get('password')
            validated_data['password'] = make_password(password)

            return User.objects.create(**validated_data)

