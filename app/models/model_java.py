# --*-- coding: utf-8  --*--
from encodings.utf_8 import encode


from django.db import models
from oauth_provider.tests.protocol import User


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
    comment = models.TextField(max_length=1000)

    def encode(self):
        return encode(self.comment)