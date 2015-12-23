# coding: utf-8

from rest_framework import routers
from app.views.set_view_basic import BasicViewSet

router = routers.DefaultRouter()
router.register(r'basic', BasicViewSet)
