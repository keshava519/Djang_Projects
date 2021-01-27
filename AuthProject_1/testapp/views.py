from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')



@login_required
def Java_view(request):
    return render(request,'testapp/java.html')

@login_required
def Python_view(request):
    return render(request,'testapp/python.html')

@login_required
def Aptitude_view(request):
    return render(request,'testapp/aptitude.html')

def Logout_view(request):
    return render(request,'testapp/logout.html')

def SignUpForm_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        #form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
