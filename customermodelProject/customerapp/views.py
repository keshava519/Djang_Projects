from django.shortcuts import render
from customerapp.models import Customerinfo

# Create your views here.

def index(request):
    return render(request,'customerapp/index.html')

def customerview(request):
    customer_list=Customerinfo.objects.all()
    my_dict={'customer_list':customer_list}
    return render(request,'customerapp/custo.html',context=my_dict)
