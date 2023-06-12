from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.academics.models import Teacher


@register(Teacher)
class TeacherAdmin(ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
    )
    icon_name = 'assignment_ind'
