from django.contrib import admin
from StudentApp.models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

# Register your models here.
admin.site.register(StudentModel,StudentAdmin)
