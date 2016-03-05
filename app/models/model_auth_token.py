#--*-- coding: utf-8 --*--

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class UserModel(models.Model):


    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        """
        ユーザ新規作成時に、自動に Token を発行
        :param sender:
        :param instance:
        :param created:
        :param kwargs:
        :return:
        """

        # ユーザデータModel
        name = models.CharField(max_length=200)
        id = models.IntegerField(max_length=100, default=0)
        email = models.EmailField(max_length=200)
        image = models.ImageField()


        if created:
            Token.objects.create(user=instance)

        for user in User.objects.all():
            Token.objects.get_or_create(user=user)


        def encode(self):
            return self.name
