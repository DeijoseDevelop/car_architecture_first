from django.urls import path
from apps.users.api.views import (
    CreateUserAPIView,
    ValidateIfUserAlreadyExist,
)


urlpatterns = [
    path(
        "create/",
        CreateUserAPIView.as_view(),
        name="Create User"
    ),
    path(
        "validate/",
        ValidateIfUserAlreadyExist.as_view(),
        name="Validate User"
    ),
]

