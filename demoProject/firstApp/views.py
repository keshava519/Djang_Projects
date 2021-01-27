from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='Helle Friends this is my first web application'

    return HttpResponse(s)
