from django.contrib import admin
from .models import Student,School
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']  # Display these fields in the list view

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'roll', 'email', 'school']