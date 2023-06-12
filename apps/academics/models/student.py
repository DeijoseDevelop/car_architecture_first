from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.academics.models import AbstractTypeUser


class Student(AbstractTypeUser):

    career = models.CharField(
        _("Career"),
        max_length=200,
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

