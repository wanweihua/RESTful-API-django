# --*-- coding:utf8 --*--
"""
辞書view
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from app.models.dictionary.model_dictionary import DictionaryModel
from app.serializers.dictionary.serializer_dictionary import DictionarySerializer


class DictionaryViewSet(viewsets.ModelViewSet):
    """
    辞書ViewSetクラス
    """

    queryset = DictionaryModel.objects.all()
    serializer_class = DictionarySerializer

    @api_view(['GET','POST'])
    def get(self, requset, format=None):
        """
        GETメソド
        :param requset:
        :param format:
        :return:
        """
        model_data = DictionaryModel.objects.all()
        serializer = DictionarySerializer(model_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST method
        :param request:
        :param format:
        :return:
        """
        serializer = DictionarySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
