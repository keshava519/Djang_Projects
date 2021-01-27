from django.contrib import admin
from testapp.models import FilterModel

# Register your models here.
class FilterAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']

admin.site.register(FilterModel,FilterAdmin)
