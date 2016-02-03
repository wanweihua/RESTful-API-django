# --*-- coding: utf-8  --*--
from encodings.utf_8 import encode
from django.contrib.auth.models import User

from django.db import models


class BasicJava(models.Model):
    """
    Javaプログラミング基礎ステップ
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def encode(self):
        return encode(self.title, self.description)


class TimeLineJava(models.Model):
    """
    タイムラインページModel
    Java プログラミング
    """
    first_name = User.first_name
    comment = models.TextField(max_length=1000)

    def encode(self):
        return encode(self.first_name, self.comment)