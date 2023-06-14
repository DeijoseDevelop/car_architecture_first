from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.students.models import Student
from apps.teachers.models import Teacher


class Course(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        _('Description'),
    )

    students = models.ManyToManyField(
        Student,
        verbose_name=_('Students'),
    )

    teachers = models.ManyToManyField(
        Teacher,
        verbose_name=_('Teachers'),
    )

    def __str__(self):
        return self.name

