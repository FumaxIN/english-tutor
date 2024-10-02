from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from tutor.models import User, Error
from tutor.serializers import UserSerializer


class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer