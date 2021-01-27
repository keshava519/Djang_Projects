from django.shortcuts import render
from testapp.models import FilterModel

# Create your views here.
def upper_view(request):
    view_list=FilterModel.objects.all()
    return render(request,'testapp/upper.html',{'view_list':view_list})


def lower_view(request):
    view_list=FilterModel.objects.all()
    return render(request,'testapp/lower.html',{'view_list':view_list})
