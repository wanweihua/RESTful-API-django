# --*-- coding:utf8 --*--
"""
1,辞書モデル
2,コンピュータサイエンス辞書
3,ユーザのデータを内部結合してデータにする
"""
from django.db import models


class DictionaryModel(models.Model):
    """
    辞書モデルclass
    """

    words = models.CharField(max_length=100)
    contents = models.TextField()

    def __encode__(self):
        return self.words, self.contents
