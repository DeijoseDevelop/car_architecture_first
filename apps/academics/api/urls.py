from django.urls import path
from apps.academics.api.views import *


urlpatterns = [
    path(
        "user/create/",
        CreateUserAPIView.as_view(),
        name="Create User"
    ),
    path(
        "user/validate/",
        ValidateIfUserAlreadyExist.as_view(),
        name="Validate User"
    ),
    path(
        "student/list/",
        ListStudentsAPIView.as_view(),
        name="List Students"
    ),
]