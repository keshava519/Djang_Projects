from django.db import models
from django import forms
from django.forms import ModelForm
from testapp.models import Student

class StudentForm(ModelForm):
    class Meta:
        form=Student
        fields='__all__'
