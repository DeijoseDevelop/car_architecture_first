from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.academics.models import Student, Course
from utils.validators.qualification_validator import qualification_validator


class Qualification(models.Model):

    student = models.ForeignKey(
        Student,
        verbose_name=_('Student'),
        on_delete=models.PROTECT,
    )

    course = models.ForeignKey(
        Course,
        verbose_name=_("Course"),
        on_delete=models.PROTECT,
    )

    value = models.FloatField(
        _("Value"),
        validators=[qualification_validator]
    )

    qualification_date = models.DateTimeField(
        _("Qualification Date"),
    )

    def __str__(self):
        return "{}".format(self.value)
