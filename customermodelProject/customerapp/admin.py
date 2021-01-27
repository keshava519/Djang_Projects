from django.contrib import admin
from customerapp.models import Customerinfo

class CustomerAdmin(admin.ModelAdmin):
    list_display=['cname','clocaton','cage','cno']

# Register your models here.
admin.site.register(Customerinfo,CustomerAdmin)
