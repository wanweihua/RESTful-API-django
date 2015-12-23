# --*-- coding: utf-8  --*--

from django.shortcuts import render
from rest_framework import viewsets
from app.models.content_basic import Basic
from app.models.serializer_basic import BasicSerializer


class BasicViewSet(viewsets.ModelViewSet):
    """
        ViewSet の定義
        modelのクエリセット
    """
    queryset = Basic.objects.all()
    serializer_class = BasicSerializer