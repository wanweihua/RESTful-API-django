# coding: utf-8

from rest_framework import routers
from app.views.set_view_basic import BasicViewSetJava, BasicViewSetPython

# java routers
java_router = routers.DefaultRouter()
java_router.register(r'basic', BasicViewSetJava)

# python routers
python_router = routers.DefaultRouter()
python_router.register(r'basic', BasicViewSetPython)

