# --*-- coding: utf-8  --*--

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.content_java import BasicJava
from app.serializers.serializer_java import BasicSerializerJava


class BasicViewSetJava(viewsets.ModelViewSet):
    """
    JavaViewSet の定義
    modelのクエリセット
    """
    queryset = BasicJava.objects.all()
    serializer_class = BasicSerializerJava


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):
        """
        GET method
        :param request:
        :param format:
        :return:
        """
        java_basic = BasicJava.objects.all()
        serializer = BasicSerializerJava(java_basic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerJava(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)