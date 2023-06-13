from rest_framework import serializers

from apps.teachers.models import Teacher


class ListTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'