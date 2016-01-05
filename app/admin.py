# --*-- coding: utf-8 --*--

from django.contrib import admin
from app.models.content_basic import BasicJava, BasicPython


@admin.register(BasicJava)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(BasicPython)
class PythonAdmin(admin.ModelAdmin):
    pass