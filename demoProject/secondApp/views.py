from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def myvillage(request):

    s='<h1> my village is very beatiful I feel peace at my Home</h1>'
    return HttpResponse(s)
