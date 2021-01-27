from django.contrib import admin
from fakerjobsApp.models import Hydjobs


class HydAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']



# Register your models here.
admin.site.register(Hydjobs,HydAdmin)
