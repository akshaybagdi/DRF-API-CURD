"""
URL configuration for mysite2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from api2.views import api2, school_list, school_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api2.urls')),
    # path('api/students/<int:pk>/', api2),  # For student detail API
    # path('api/schools/', school_list),  # For school list and creation
    # path('api/schools/<int:pk>/', school_detail),


]
