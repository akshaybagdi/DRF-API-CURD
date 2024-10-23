from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api2(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                student = Student.objects.get(pk=pk)  # Get the specific student
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'Error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        if pk is not None:
            try:
                instance = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response({'Error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = StudentSerializer(instance, data=request.data, partial=(request.method == 'PATCH'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': 'ID must be provided'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                instance = Student.objects.get(pk=pk)  # Get the specific student
                instance.delete()  # Delete the student
                return Response({'Message': 'Student deleted successfully'},
                                status=status.HTTP_204_NO_CONTENT)  # Return no content
            except Student.DoesNotExist:
                return Response({'Error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Error': 'ID must be provided'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def school_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                school = School.objects.get(pk=pk)
                serializer = SchoolSerializer(school)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except School.DoesNotExist:
                return Response({'Error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        queryset = School.objects.all()
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'DELETE']:
        if pk is not None:
            try:
                school = School.objects.get(pk=pk)
            except School.DoesNotExist:
                return Response({'Error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
            if request.method == 'PUT':
                serializer = SchoolSerializer(school, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                school.delete()
                return Response({'Message': 'School deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'Error': 'ID must be provided'}, status=status.HTTP_400_BAD_REQUEST)