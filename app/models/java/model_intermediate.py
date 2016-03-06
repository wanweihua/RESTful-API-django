# --*-- coding: utf8 --*--

"""
Java中級
"""
from django.db import models

class IntermediateModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()


    def encode(self):
        return  self.title, self.description