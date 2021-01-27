from django.shortcuts import render,redirect
from testapp.models import EmployeeModel
from testapp.forms import EmployeeForm

# Create your views here.
def retrieve_view(request):
    employee_object=EmployeeModel.objects.all()
    return render(request,'testapp/index.html',{'employee_object':employee_object})


def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render (request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    employee=EmployeeModel.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employees=EmployeeModel.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employees)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'employees':employees})
