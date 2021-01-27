import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','keshava_faker_jobsportal_Project.settings')
import django
django.setup()


from fakerjobsApp.models import *
from faker import Faker
from random import *
fake =Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('M.tech','B.tech','P.hd','MBA','MCA'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=fake.phonenumbergen()
        hydjobs_record=Hydjobs.objects.get_or_create(date=fdate,
                                                     company=fcompany,
                                                     title=ftitle,
                                                     eligibility=feligibility,
                                                     address=faddress,
                                                     email=femail,
                                                     phonenumber=fphonenumber)
populate(25)
