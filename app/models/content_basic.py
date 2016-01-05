# --*-- coding: utf-8  --*--

from django.db import models


class BasicJava(models.Model):
    """
        Javaプログラミング基礎ステップ
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title, self.description



class BasicPython(models.Model):
    """
        Pythonプログラミング基礎
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title, self.description

