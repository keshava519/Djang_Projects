from django.db import models

# Create your models here.
class Job(models.Model):
    jobdate=models.DateField()
    location=models.CharField(max_length=30)
    offeredsalary=models.FloatField()
    qualification=models.CharField(max_length=30)

    def __str__(self):
        return self.location
