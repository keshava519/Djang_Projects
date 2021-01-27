from django.contrib import admin
from testapp.models import EmployeeModel

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(EmployeeModel,EmployeeAdmin)
