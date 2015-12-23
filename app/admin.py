# --*-- coding: utf-8 --*--

from django.contrib import admin
from app.models.content_basic import Basic


@admin.register(Basic)
class UserAdmin(admin.ModelAdmin):
    pass