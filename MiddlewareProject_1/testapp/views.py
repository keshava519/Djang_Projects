from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_view(request):
    print('This line printed by view function')
    return HttpResponse ('<h1>DEMO MIDDLEWARE Application</h1>')
