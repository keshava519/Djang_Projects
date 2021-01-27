from django.shortcuts import render
from StudentApp import forms



# Create your views here.
def StudentView(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'StudentApp/student.html',{'form':form})
