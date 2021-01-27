from django.shortcuts import render
from testapp.models import EmployeeModel
from django.db.models import Q
from django.db.models import Avg,Min,Max,Sum,Count

# Create your views here.
def Employee_View(request):
    employees=EmployeeModel.objects.all()
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',context=my_dict)
