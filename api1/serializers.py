
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Student
#         fileds=['roll','city']
#         read_only_fields=['name']