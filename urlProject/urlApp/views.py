from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstappinfo(request):
    s='<h1> First Application Information</h1>'
    return HttpResponse(s)

def secondappinfo(request):
    s='<h1> Second Application Information</h1>'
    return HttpResponse(s)

def thirdappinfo(request):
    s='<h1> Third Application Information</h1>'
    return HttpResponse(s)

def fourthappinfo(request):
    s='<h1> Fourth Application Information</h1>'
    return HttpResponse(s)
