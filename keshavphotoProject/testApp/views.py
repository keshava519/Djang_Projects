from django.shortcuts import render

# Create your views here.
def home(reuest):
    return render(reuest,'testApp/home.html')

def profile(request):
    return render(request,'testApp/profile.html')
