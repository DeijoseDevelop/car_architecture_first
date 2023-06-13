from rest_framework import serializers

from apps.courses.models import Course
from apps.students.models import Student
from apps.students.api.serializers import ListStudentSerializer
from apps.teachers.models import Teacher
from apps.teachers.api.serializers import ListTeacherSerializer


class ListCourseSerializer(serializers.ModelSerializer):

    students = ListStudentSerializer(read_only=True, many=True)
    teachers = ListTeacherSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'


class ListCourseWithoutStudentsAndTeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'description',)