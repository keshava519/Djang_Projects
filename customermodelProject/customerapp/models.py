from django.db import models

# Create your models here.
class Customerinfo(models.Model):
    cname=models.CharField(max_length=30)
    cage=models.IntegerField()
    cno=models.IntegerField()
    clocaton=models.CharField(max_length=30)

    def __str__(self):
        return self.cname
