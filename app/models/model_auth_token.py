#--*-- coding: utf-8 --*--

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from rest_framework.authtoken.models import Token


class UserModel(models.Model):

    name = models.CharField(max_length=80)

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
        if created:
            Token.objects.create(user=instance)

