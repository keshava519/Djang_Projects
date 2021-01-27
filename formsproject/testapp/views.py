from django.shortcuts import render
from . import forms


# Create your views here.
def Studentview(request):
    form=forms.StudentForm()
    return render(request,'testapp/test.html',{'form':form})
