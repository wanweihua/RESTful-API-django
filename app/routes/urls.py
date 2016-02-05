# coding: utf-8

from rest_framework import routers

# java routers
from app.views.android.set_view_android import BasicViewSetAndroid
from app.views.java.set_view_java import BasicViewSetJava
from app.views.java.set_view_java import JavaTimeLine
from app.views.python.set_view_python import BasicViewSetPython
from app.views.python.set_view_python import PythonTimeLine

java_router = routers.DefaultRouter()
java_router.register(r'basic', BasicViewSetJava)
java_time = routers.DefaultRouter()
java_time.register(r'timeline', JavaTimeLine)


# python routers
python_router = routers.DefaultRouter()
python_router.register(r'basic', BasicViewSetPython)
python_time = routers.DefaultRouter()
python_router.register(r'timeline', PythonTimeLine)


# android routers
android_router = routers.DefaultRouter()
android_router.register(r'basic', BasicViewSetAndroid)

