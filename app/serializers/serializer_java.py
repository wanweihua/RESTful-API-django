# --*-- coding: utf-8 --*--
import json
from rest_framework import serializers
from app.models.model_java import BasicJava


class BasicSerializerJava(serializers.ModelSerializer):
    """
    シリアライズの定義(Java)
    serializer.ModelSerializer を継承
    filed = API
    """
    class Meta:
        model = BasicJava
        filed = (u'title', u'description')
