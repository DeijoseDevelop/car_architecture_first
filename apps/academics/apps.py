from django.apps import AppConfig


app_name = 'academics'

class AcademicsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics'
    verbose_name = "Academics"
    icon_name = 'account_balance'