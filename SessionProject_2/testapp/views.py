from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,GfForm

def Name_View(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def Age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form})

def Gfname_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=GfForm()
    return render(request,'testapp/gfname.html',{'form':form})

def Result_View(request):
    gfname=request.GET['gfname']
    request.session['gfname']=gfname
    return render(request,'testapp/result.html')
