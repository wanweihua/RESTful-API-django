# --*-- coding: utf-8 --*--
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models.model_auth_token import UserModel
from app.permissions import IsAuthenticatedOrCreate
from app.serializers.serializer_auth import SignUpSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

    def pre_save(self, object):
        object.owner = self.request.user

    def get(self,request):
        """
        GET method allow
        :param request:
        :return:
        """
        login_data = UserModel.objects.all()
        serializer = SignUpSerializer(login_data, many=True)
        return Response(serializer.data)


    def post(self, request, *args):
        """
        POST method
        :param request:
        :param args:
        :return:
        """

        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


