from django.contrib import admin
from testApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','smarks','sgrade']

# Register your models here.
admin.site.register(Student,StudentAdmin)
