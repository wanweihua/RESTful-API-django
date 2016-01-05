# coding: utf-8

from rest_framework import routers
from app.views.set_view_android import BasicViewSetAndroid
from app.views.set_view_java import BasicViewSetJava
from app.views.set_view_python import BasicViewSetPython


# java routers
java_router = routers.DefaultRouter()
java_router.register(r'basic', BasicViewSetJava)


# python routers
python_router = routers.DefaultRouter()
python_router.register(r'basic', BasicViewSetPython)


# android routers
android_router = routers.DefaultRouter()
android_router.register(r'basic', BasicViewSetAndroid)

