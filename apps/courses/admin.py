from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.courses.models import Course


@register(Course)
class CourseAdmin(ModelAdmin):

    list_display = (
        'name',
        'description',
    )
    icon_name = 'book'








