from django.urls import path
from apps.students.api.views import (
    ListStudentsAPIView,
)


urlpatterns = [
    path(
        "list/",
        ListStudentsAPIView.as_view(),
        name="List Students"
    ),
]
