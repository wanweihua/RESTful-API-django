# --*-- coding: utf-8 --*--

from rest_framework import serializers
from app.models.content_python import BasicPython


class BasicSerializerPython(serializers.ModelSerializer):
    """
        シリアライズの定義(Python)
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = BasicPython
        filed = (u'title', u'description')
