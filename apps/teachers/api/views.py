from rest_framework import generics, views, status
from django_filters.rest_framework import DjangoFilterBackend

from utils.mixins import *
from apps.teachers.models import Teacher
from apps.teachers.api.serializers import ListTeacherSerializer

class ListTeachersAPIView(APIKeyRequiredMixin, generics.ListAPIView):

    serializer_class = ListTeacherSerializer
    queryset = Teacher.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['document_number']

