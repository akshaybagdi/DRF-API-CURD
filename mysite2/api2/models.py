from django.db import models

from django.db import models

class School(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()
    email = models.EmailField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

