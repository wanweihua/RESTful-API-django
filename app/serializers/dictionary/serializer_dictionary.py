# --*-- coding: utf-8 --*--

from rest_framework import serializers
from app.models.dictionary.model_dictionary import DictionaryModel


class DictionarySerializer(serializers.ModelSerializer):
    """
    シリアライズ辞書
    """
    class Meta:
        model = DictionaryModel
        filed = (u'words', u'contents')

