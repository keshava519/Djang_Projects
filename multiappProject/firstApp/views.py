from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstappinfo(request):
    return HttpResponse('<h1> Firstapp Created</h1>')
