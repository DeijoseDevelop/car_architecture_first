from django.urls import path
from apps.qualifications.api.views import (
    ListQualificationsAPIView,
)


urlpatterns = [
    path(
        "list/",
        ListQualificationsAPIView.as_view(),
        name="List Qualification"
    ),
]
