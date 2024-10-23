from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_list(request,pk):
    stu=Student.objects.get(id=pk)
    # print(stu)
    seriaizer=StudentSerializer(stu)
    # print(seriaizer)
    # print(seriaizer.data)
    # json_data=JSONRenderer().render(seriaizer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')

### Quersy Set- All sets

def student_list(request):
    stu=Student.objects.all()
    # print(stu)
    seriaizer=StudentSerializer(stu, many=True)
    # print(seriaizer)
    # print(seriaizer.data)
    json_data=JSONRenderer().render(seriaizer.data)
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')

