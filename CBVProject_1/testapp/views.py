from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
class Helloworld_View(View):
    def get(self,request):
        return HttpResponse('<h1> Hello World Class Based View</h1>')

class Template_View(TemplateView):
    template_name='testapp/result.html'
