# --*-- coding:utf8 --*--
from rest_framework import serializers
from app.models.user_image.model_user_image import UserImageModel


class UserImageSerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = UserImageModel
         field = (u'user_image')