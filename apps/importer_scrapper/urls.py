from django.urls import path

from apps.importer_scrapper.views import (
    HomeView,
    ExternalLoginView,
    ExternalLogoutView,
    ReadFileView,
    ScrapperView,
)


urlpatterns = [
    path(
        'home/',
        HomeView.as_view(),
        name="home"
    ),

    path(
        'login/',
        ExternalLoginView.as_view(),
        name="login"
    ),

    path(
        'logout/',
        ExternalLogoutView.as_view(),
        name="logout"
    ),

    path(
        'readfile/',
        ReadFileView.as_view(),
        name="readfile"
    ),

    path(
        'scrapper/',
        ScrapperView.as_view(),
        name="scrapper"
    ),
]
