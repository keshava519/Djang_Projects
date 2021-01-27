from django.shortcuts import render
from fakerjobsApp.models import *

# Create your views here.
def index(request):
    return render(request,'fakerjobsApp/index.html')


def hydjobsview(request):
    hydjobs_list=Hydjobs.objects.order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render (request,'fakerjobsApp/hydjobs.html',context=my_dict)
