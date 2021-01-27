from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hydjobsinfo(request):
    s='<h1> Hyderabad jobs:</h1>'
    return HttpResponse(s)

def bangalorejobsinfo(request):
    s='<h1> Bangalore jobs:</h1>'
    return HttpResponse(s)

def chennaijobsinfo(request):
    s='<h1> Chennai jobs:</h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s='<h1> Pune jobs:</h1>'
    return HttpResponse(s)
