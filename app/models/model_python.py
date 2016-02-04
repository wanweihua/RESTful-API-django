# --*-- coding: utf-8 --*--
from encodings.utf_8 import encode
from urllib import urlencode
import urllib
from django.db import models


class BasicPython(models.Model):
    """
        Pythonプログラミング基礎
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def encode(self):
        return encode(self.title, self.description)


class TimeLinePython(models.Model):
    """
        python Timeline
    """
    comment = models.TextField(max_length=1000)

    def encode(self):
        return encode(self.comment)
