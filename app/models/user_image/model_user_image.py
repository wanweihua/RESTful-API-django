# --*-- coding:utf8 --*--
from django.db import models
from app.views.user_image.set_view_image import UserImageView


class UserImageModel(models.Model):

    @UserImageView.delete_previous_image
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(UserImageModel, self).save()


    @UserImageView.delete_previous_image
    def delete(self, using=None, keep_parents=False):
        super(UserImageModel, self).delete()



    user_image = models.ImageField('ユーザ画像', upload_to=UserImageView.get_image)