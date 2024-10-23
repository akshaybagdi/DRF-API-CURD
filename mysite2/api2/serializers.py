from rest_framework import serializers
from .models import Student,School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    school = SchoolSerializer(read_only=True)


    def create(self, validated_data):

        school_data = validated_data.pop('school')# Extract the school data from the validated data
        # Check if the school already exists or create a new one
        school, created = School.objects.get_or_create(
            name=school_data.get('name'),
            defaults={'address': school_data.get('address')}
        )
        student = Student.objects.create(school=school, **validated_data)
        return student

