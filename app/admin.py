# --*-- coding: utf-8 --*--

from django.contrib import admin
from app.models.model_android import BasicAndroid
from app.models.model_java import BasicJava
from app.models.model_python import BasicPython


@admin.register(BasicJava)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(BasicPython)
class PythonAdmin(admin.ModelAdmin):
    pass


@admin.register(BasicAndroid)
class AndroidAdmin(admin.ModelAdmin):
    pass
