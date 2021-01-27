from django.db import models

# Create your models here.
class ConductInfo(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    addr=models.CharField(max_length=250)
    class Meta:
        abstract=True

class Student(ConductInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ConductInfo):
    sub=models.CharField(max_length=60)
    sal=models.FloatField()
