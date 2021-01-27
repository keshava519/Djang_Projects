from django.shortcuts import render

# Create your views here.
def praticewish(request):
    return render(request,'templateApp/wish.html')
