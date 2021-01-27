from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book

# Create your views here.
class Book_ListView(ListView):
    model=Book
    #default html file name is book_list.html we have to Create
    #default context name is book_list
    #template_name='testapp/bookinfo.html'
    #context_object_name='list_of_books'


class Book_DetailView(DetailView):
    model=Book
