# --*-- coding: utf-8 --*--
from rest_framework import serializers
from app.models.android.model_android import BasicAndroid


class BasicSerializerAndroid(serializers.ModelSerializer):
    """
        シリアライズの定義(Android)
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = BasicAndroid
        filed = (u'title', u'description')
