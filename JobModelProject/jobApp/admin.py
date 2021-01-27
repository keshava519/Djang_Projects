from django.contrib import admin
from jobApp.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display=['jobdate','offeredsalary','qualification','location']


# Register your models here.
admin.site.register(Job,JobAdmin)
