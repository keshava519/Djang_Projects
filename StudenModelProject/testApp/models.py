from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    smarks=models.IntegerField()
    sgrade=models.FloatField()

    def __str__(self):
        return self.sname
