# --*-- coding: utf-8 --*--
from rest_framework import viewsets
from app.models.content_android import BasicAndroid
from app.serializers.serializer_android import BasicSerializerAndroid


class BasicViewSetAndroid(viewsets.ModelViewSet):
    """
        PythonViewSet の定義
        modelのクエリセット
    """
    queryset = BasicAndroid.objects.all()
    serializer_class = BasicSerializerAndroid
