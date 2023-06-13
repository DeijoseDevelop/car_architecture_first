from rest_framework import generics, views, status
from django_filters.rest_framework import DjangoFilterBackend

from utils.mixins import *
from apps.qualifications.models import Qualification
from apps.qualifications.api.serializers import ListQualificationsSerializer

class ListQualificationsAPIView(APIKeyRequiredMixin, generics.ListAPIView):

    serializer_class = ListQualificationsSerializer
    queryset = Qualification.objects.all()

