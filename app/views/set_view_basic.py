# --*-- coding: utf-8  --*--

from django.shortcuts import render
from rest_framework import viewsets
from app.models.content_basic import BasicJava, BasicPython
from app.models.serializer_basic import BasicSerializerJava, BasicSerializerPython


class BasicViewSetJava(viewsets.ModelViewSet):
    """
        JavaViewSet の定義
        modelのクエリセット
    """
    queryset = BasicJava.objects.all()
    serializer_class = BasicSerializerJava


class BasicViewSetPython(viewsets.ModelViewSet):
    """
        PythonViewSet の定義
        modelのクエリセット
    """
    queryset = BasicPython.objects.all()
    serializer_class = BasicSerializerPython
