from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.academics.models import User


@register(User)
class UserAdmin(ModelAdmin):

    list_display = (
        'email',
        'is_staff',
        'last_login',
    )
