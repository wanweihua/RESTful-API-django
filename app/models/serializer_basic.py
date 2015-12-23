# --*-- coding: utf-8 --*--
from rest_framework import serializers
from app.models.content_basic import Basic


class BasicSerializer(serializers.ModelSerializer):
    """
        シリアライズの定義
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = Basic
        filed = ('title', 'description')
