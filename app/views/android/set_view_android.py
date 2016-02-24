# --*-- coding: utf-8 --*--

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.android.model_android import BasicAndroid
from app.serializers.android.serializer_android import BasicSerializerAndroid


class BasicViewSetAndroid(viewsets.ModelViewSet):
    """
        PythonViewSet の定義
        modelのクエリセット
    """
    queryset = BasicAndroid.objects.all()
    serializer_class = BasicSerializerAndroid


    @api_view(['GET', 'POST'])
    def get(self, request, format=None):
        """
        GET method
        :param request:
        :param format:
        :return:
        """
        model_data = BasicAndroid.objects.all()
        serializer = BasicSerializerAndroid(model_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerAndroid(data=request.data)

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
        model_data = self.get_object(pk)
        model_data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        """
        PUT method
        :param request:
        :param format:
        :return:
        """
        serializer = BasicSerializerAndroid(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
