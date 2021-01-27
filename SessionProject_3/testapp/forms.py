from django import forms


class FormItem(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
