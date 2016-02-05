# --*-- coding: utf-8 --*--
import json
from rest_framework import serializers
from app.models.java.model_java import BasicJava, TimeLineJava


class BasicSerializerJava(serializers.ModelSerializer):
    """
    シリアライズの定義(Java)
    serializer.ModelSerializer を継承
    filed = API
    """
    class Meta:
        model = BasicJava
        filed = (u'title', u'description')


class SerializerJavaTimeLine(serializers.ModelSerializer):
    """
    シリアライズ定義(Javaのタイムライン)
    """
    class Meta:
        model = TimeLineJava
        field = (u'first_name', u'comment')
