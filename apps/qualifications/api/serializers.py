from rest_framework import serializers

from apps.qualifications.models import Qualification
from apps.students.models import Student
from apps.students.api.serializers import ListStudentSerializer
from apps.courses.models import Course
from apps.courses.api.serializers import (
    ListCourseSerializer,
    ListCourseWithoutStudentsAndTeachersSerializer,
)


class ListQualificationsSerializer(serializers.ModelSerializer):

    # course = ListCourseSerializer(read_only=True)
    # student = ListStudentSerializer(read_only=True)

    # class Meta:
    #     model = Qualification
    #     fields = ('value', 'qualification_date',)

    course = ListCourseWithoutStudentsAndTeachersSerializer(read_only=True)
    student = ListStudentSerializer(read_only=True)

    class Meta:
        model = Qualification
        fields = '__all__'