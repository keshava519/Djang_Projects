from django.shortcuts import render
from testapp import forms


# Create your views here.
def StudentView(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Data inserted successfully')
    return render(request,'testapp/test.html',{'form':form})
