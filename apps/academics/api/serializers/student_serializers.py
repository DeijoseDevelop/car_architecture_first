from rest_framework import serializers

from apps.academics.models import Student


class ListStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'