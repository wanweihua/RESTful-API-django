# --*-- coding: utf-8 --*--

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.python.model_python import BasicPython, TimeLinePython
from app.serializers.python.serializer_python import BasicSerializerPython, SerializerPythonTimeLine


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

    def delete(self, request, pk, format=None):
        """
        DELETE method
        :param request:
        :param format:
        :return:
        """
        python_basic = self.get_object(pk)
        python_basic.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        """
        PUT method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerPython(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PythonTimeLine(viewsets.ModelViewSet):
    """
    PythonTimeLineのView
    modelクエリ
    """

    queryset = TimeLinePython.objects.all()
    serializer_class = SerializerPythonTimeLine


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):
        """
        GET
        :param request:
        :param format:
        :return:
        """

        timeline_data = TimeLinePython.objects.all()
        serializer = SerializerPythonTimeLine(timeline_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST method
        :param request:
        :param format:
        :return:
        """

        serializer = SerializerPythonTimeLine(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, format=None):
        """
        DELETE method
        :param request:
        :param format:
        :return:
        """

        comment_data = self.get_object()
        comment_data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, format=None):
        """
        PUT method
        :param request:
        :param format:
        :return:
        """

        serializer = SerializerPythonTimeLine(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

