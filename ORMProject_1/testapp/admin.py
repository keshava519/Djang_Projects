from django.contrib import admin
from testapp.models import EmployeeModel,ProxyEmployeeModel_1,ProxyEmployeeModel_2

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployeeAdmin2(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(EmployeeModel,EmployeeAdmin)
admin.site.register(ProxyEmployeeModel_1,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployeeModel_2,ProxyEmployeeAdmin2)
