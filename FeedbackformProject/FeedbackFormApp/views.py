from django.shortcuts import render
from . import forms

# Create your views here.

def Thankyou_view(request):
    return render(request,'FeedbackFormApp/thankyou.html')


def FeedbackForm_view(request):
    if request.method=='GET':
        form=forms.FeedbackForm()
        return render(request,'FeedbackFormApp/fb.html',{'form':form})

    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form is successfully validate')
            print(' Student Name:',form.cleaned_data['name'])
            print(' Student Roll Number:',form.cleaned_data['rollno'])
            print(' Student Email:',form.cleaned_data['email'])
            print(' Student Feedback:',form.cleaned_data['feedback'])
            return Thankyou_view(request)
    return render(request,'FeedbackFormApp/fb.html',{'form':form})
