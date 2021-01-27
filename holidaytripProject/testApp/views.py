from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def forest(request):
    return render(request,'testApp/forest.html')

def temple(request):
    return render(request,'testApp/temple.html')

def beach(request):
    return render(request,'testApp/beach.html')
