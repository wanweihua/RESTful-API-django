# --*-- coding: utf-8 --*--
from encodings.utf_8 import encode

from django.db import models


class BasicAndroid(models.Model):
    """
        Androidプログラミング基礎
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def encode(self):
        return encode(self.title, self.description)



