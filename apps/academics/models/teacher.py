from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.academics.models import AbstractTypeUser


class Teacher(AbstractTypeUser):

    specialty = models.CharField(
        _("Specialty"),
        max_length=100,
    )

    experience = models.TextField(
        _("Experience"),
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
