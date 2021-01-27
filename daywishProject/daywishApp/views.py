from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1>Hello Good Morning hava fun today</h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1>Hello Good Afternoon have a luch</h1>')

def good_evening_view(request):
    return HttpResponse('<h1>Hello Good Evening hava snaks</h1>')

def good_night_view(request):
    return HttpResponse('<h1>Hello time to sleep Good night </h1>')
