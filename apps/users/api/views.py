import json

from django.contrib.auth.hashers import make_password
from rest_framework import generics, views, status
from rest_framework.response import Response

from utils.exceptions import (
    GeneralAPIException,
    RequiredFieldInParams,
    InvalidPassword,
)
from utils.custom import JWTMaker
from utils.mixins import *
from apps.users.api.serializers import (
    CreateUserSerializer,
    ValidateUserSerializer,
)
from apps.users.models import User


class CreateUserAPIView(APIKeyRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        jwt_maker = JWTMaker()

        request.data["password"] = make_password(request.data["password"])
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        response = {
            "token": jwt_maker.generate_jwt({
                "email": serializer.data.get("email")
            }),
            **serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class ValidateIfUserAlreadyExist(APIKeyRequiredMixin, generics.GenericAPIView):

    serializer_class = ValidateUserSerializer

    def post(self, request, *args, **kwargs):
        print(f"BODY: {request.data}")
        if not 'email' in request.data:
            raise RequiredFieldInParams('email')

        try:
            email = request.data.get('email')
            user = User.objects.get(email=email)
            serializer = self.get_serializer(user)

            if not user.check_password(request.data.get('password')):
                raise InvalidPassword()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise GeneralAPIException(
                detail="User does not exist",
                code=status.HTTP_404_NOT_FOUND,
            )
