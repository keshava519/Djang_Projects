import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMProject_1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
faker=Faker()


def populate(n):
    for i in range(n):
        feno=randint(1000,9999)
        fename=faker.name()
        fesal=randint(10000,99999)
        feaddr=faker.city()
        emp_record=EmployeeModel.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(25)
