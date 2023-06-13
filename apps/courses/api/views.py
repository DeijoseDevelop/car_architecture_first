from rest_framework import generics, views, status
from django_filters.rest_framework import DjangoFilterBackend

from utils.mixins import *
from apps.courses.models import Course
from apps.courses.api.serializers import ListCourseSerializer

class ListCoursesAPIView(APIKeyRequiredMixin, generics.ListAPIView):

    serializer_class = ListCourseSerializer
    queryset = Course.objects.all()

