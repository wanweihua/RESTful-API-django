# --*-- coding: utf-8  --*--

from django.shortcuts import render
from rest_framework import viewsets
from app.models.content_java import BasicJava
from app.models.serializer_java import BasicSerializerJava


class BasicViewSetJava(viewsets.ModelViewSet):
    """
        JavaViewSet の定義
        modelのクエリセット
    """
    queryset = BasicJava.objects.all()
    serializer_class = BasicSerializerJava
