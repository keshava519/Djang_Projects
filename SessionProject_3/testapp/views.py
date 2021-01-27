from django.shortcuts import render
from testapp.forms import FormItem

# Create your views here.
def AddItem_view(request):
    form=FormItem()
    if request.method=="POST":
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity

    return render(request,'testapp/additem.html',{'form':form})

def displayItem_view(request):
    return render(request,'testapp/displayitem.html')
