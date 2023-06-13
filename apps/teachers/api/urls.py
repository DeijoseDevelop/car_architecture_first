from django.urls import path
from apps.teachers.api.views import (
    ListTeachersAPIView,
)


urlpatterns = [
    path(
        "list/",
        ListTeachersAPIView.as_view(),
        name="List Teachers"
    ),
]
