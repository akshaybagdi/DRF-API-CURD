from django.urls import path
from .views import api2, school_api

urlpatterns = [
    path('students/', api2),
    path('students/<int:pk>/', api2),
    path('schools/', school_api),
    path('schools/<int:pk>/', school_api),
]
