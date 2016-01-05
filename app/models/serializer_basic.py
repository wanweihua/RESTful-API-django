# --*-- coding: utf-8 --*--
import json
from rest_framework import serializers
from app.models.content_basic import BasicJava, BasicPython


class BasicSerializerJava(serializers.ModelSerializer):
    """
        シリアライズの定義(Java)
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = BasicJava
        filed = (u'title', u'description')




class BasicSerializerPython(serializers.ModelSerializer):
    """
        シリアライズの定義(Python)
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = BasicPython
        filed = (u'title', u'description')
