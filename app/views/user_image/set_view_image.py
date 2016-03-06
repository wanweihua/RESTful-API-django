# --*-- coding:utf8 --*--

"""
ユーザの画像保存
UUIDへ変更
"""
import os
import uuid
from PIL.Image import Image
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.user_image.model_user_image import UserImageModel
from app.serializers.user_image.serializer_image import UserImageSerializer
from restful_api.settings import MEDIA_ROOT


class UserImageView(viewsets.ModelViewSet):
    """
    ユーザ画像設定する
    """
    queryset = UserImageModel.user_image
    serializer_class = UserImageSerializer


    @api_view(['GET','POST'])
    def get(self, requset, format=None):

        model_data = UserImageModel.objects.all()
        serializer = UserImageSerializer(model_data, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = UserImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get_image(self, filename):
        """
        path取得
        UUID変換
        :param filename:
        :return:
        """

        prefix = "user_image"
        image_name = str(uuid.uuid4().replace('-', ''))
        extension = os.path.splitext(filename)[-1]

        return prefix + image_name + extension



    def delete_previous_image(self, function):
        """
        古い画像の削除
        :param function:
        :return:
        """

        def wrapper(*args, **kwargs):
            self = args[0]

            result = Image.objects.fieter(pk=self.pk)
            previous = result[0] if len(result) else None
            super(Image, self).save()

            result = function(*args, **kwargs)

            if previous:
                os.remove(MEDIA_ROOT + '/' + previous.image.name)

            return result

        return wrapper()