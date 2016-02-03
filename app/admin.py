# --*-- coding: utf-8 --*--

from django.contrib import admin
from app.models.model_android import BasicAndroid
from app.models.model_auth_token import UserModel
from app.models.model_java import BasicJava, TimeLineJava
from app.models.model_python import BasicPython


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'password')
    # list_display_links = ('name', 'password',)

@admin.register(BasicJava)
class JavaAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

@admin.register(BasicPython)
class PythonAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')


@admin.register(BasicAndroid)
class AndroidAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')


@admin.register(TimeLineJava)
class TimeLineJavaAdmin(admin.ModelAdmin):
    pass

