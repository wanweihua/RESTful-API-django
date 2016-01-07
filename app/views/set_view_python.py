# --*-- coding: utf-8 --*--
from rest_framework import viewsets
from app.models.model_python import BasicPython
from app.serializers.serializer_python import BasicSerializerPython


class BasicViewSetPython(viewsets.ModelViewSet):
    """
        PythonViewSet の定義
        modelのクエリセット
    """
    queryset = BasicPython.objects.all()
    serializer_class = BasicSerializerPython
