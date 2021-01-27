from django.db import models
#from django.db.models.manager import Manager

# Create your models here.
class CustumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')

class CustumManager_1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esal')

class CustumManager_2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=90000)


class EmployeeModel(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustumManager()

class ProxyEmployeeModel_1(EmployeeModel):
    objects=CustumManager_1()
    class Meta:
        proxy=True

class ProxyEmployeeModel_2(EmployeeModel):
    objects=CustumManager_2()
    class Meta:
        proxy=True
