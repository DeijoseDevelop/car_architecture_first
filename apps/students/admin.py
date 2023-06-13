from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.students.models import Student


@register(Student)
class StudentAdmin(ModelAdmin):

    list_display = (
        'document_number',
        'first_name',
        'last_name',
        'email',
    )
    icon_name = 'school'
