from django.urls import path
from apps.courses.api.views import (
    ListCoursesAPIView,
)


urlpatterns = [
    path(
        "list/",
        ListCoursesAPIView.as_view(),
        name="List Courses"
    ),
]
