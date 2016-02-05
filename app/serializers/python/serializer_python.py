# --*-- coding: utf-8 --*--

from rest_framework import serializers
from app.models.python.model_python import BasicPython
from app.models.python.model_python import TimeLinePython


class BasicSerializerPython(serializers.ModelSerializer):
    """
        シリアライズの定義(Python)
        serializer.ModelSerializer を継承
        filed = API
    """
    class Meta:
        model = BasicPython
        filed = (u'title', u'description')


class SerializerPythonTimeLine(serializers.ModelSerializer):
    """
    シリアライズ定義(Pythonのタイムライン)
    """
    class Meta:
        model = TimeLinePython
        field = (u'first_name', u'comment')
