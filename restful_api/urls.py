"""restful_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from app.routes.urls import java_router, python_router, android_router, java_time, python_time, dictionary_router
from rest_framework.authtoken import views as auth_views
from app.views.set_view_auth import SignUp

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^sign-up/$', SignUp.as_view(), name="sign_up"),
    url(r'^api-token-auth/', auth_views.obtain_auth_token, name='auth-api'),

    url(r'^api/v1/', include(dictionary_router.urls, namespace='dictionry_api')),

    url(r'^api/v1/java/', include(java_router.urls, namespace='java_basic_api')),
    url(r'^api/v1/java/', include(java_time.urls, namespace='java_timeline_api')),

    url(r'^api/v1/python/', include(python_router.urls, namespace='python_api')),
    url(r'^api/v1/python/', include(python_time.urls, namespace='python_timeline_api')),

    url(r'^api/v1/android/', include(android_router.urls, namespace='android_api')),
]
