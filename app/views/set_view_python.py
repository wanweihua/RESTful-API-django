# --*-- coding: utf-8 --*--

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.model_python import BasicPython
from app.serializers.serializer_python import BasicSerializerPython


class BasicViewSetPython(viewsets.ModelViewSet):
    """
        PythonViewSet の定義
        modelのクエリセット
    """
    queryset = BasicPython.objects.all()
    serializer_class = BasicSerializerPython


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):
        """
        GET method
        :param request:
        :param format:
        :return:
        """
        java_basic = BasicPython.objects.all()
        serializer = BasicSerializerPython(java_basic, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        """
        POST method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerPython(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
