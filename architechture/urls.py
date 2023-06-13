from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', RedirectView.as_view(url="/admin/", permanent=True)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('apps.importer_scrapper.urls')),
    path("api/v1/users/", include("apps.users.api.urls")),
    path("api/v1/students/", include("apps.students.api.urls")),
    path("api/v1/teachers/", include("apps.teachers.api.urls")),
    path("api/v1/courses/", include("apps.courses.api.urls")),
    path("api/v1/qualifications/", include("apps.qualifications.api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
