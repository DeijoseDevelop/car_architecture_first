from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.academics.models import Qualification


@register(Qualification)
class QualificationAdmin(ModelAdmin):

    list_display = (
        'student',
        'course',
        'value',
        'qualification_date',
    )
    icon_name = 'check_circle'




