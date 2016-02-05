# --*-- coding: utf-8  --*--
from requests import delete

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.java.model_java import BasicJava, TimeLineJava
from app.serializers.java.serializer_java import BasicSerializerJava, SerializerJavaTimeLine


class BasicViewSetJava(viewsets.ModelViewSet):
    """
    JavaViewSet の定義
    modelのクエリセット
    """
    queryset = BasicJava.objects.all()
    serializer_class = BasicSerializerJava


    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
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

    def delete(self, request, pk, format=None):
        """
        DELETE method
        :param request:
        :param format:
        :return:
        """
        java_basic = self.get_object(pk)
        java_basic.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        """
        PUT method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerJava(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JavaTimeLine(viewsets.ModelViewSet):
    """
    JavaTimeLineのView
    modelクエリ
    """

    queryset = TimeLineJava.objects.all()
    serializer_class = SerializerJavaTimeLine


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):
        """
        GET
        :param request:
        :param format:
        :return:
        """

        timeline_data = TimeLineJava.objects.all()
        serializer = SerializerJavaTimeLine(timeline_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST
        :param request:
        :param format:
        :return:
        """

        serializer = SerializerJavaTimeLine(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
