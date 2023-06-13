from rest_framework import generics, views, status
from django_filters.rest_framework import DjangoFilterBackend

from utils.mixins import *
from apps.students.models import Student
from apps.students.api.serializers import ListStudentSerializer

class ListStudentsAPIView(APIKeyRequiredMixin, generics.ListAPIView):

    serializer_class = ListStudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['document_number']

