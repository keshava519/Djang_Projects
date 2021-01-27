from django import forms
from django.core import validators



class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password (again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget = forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print('Total form clean at once')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if len(inputname) <4:
            raise forms.ValidationError('Name length should be 10 chars')
        inputrollno=total_cleaned_data['rollno']
        if len(str(inputrollno)) <=2:
            raise forms.ValidationError('Please provide >2 charcters')

        inputpwd=total_cleaned_data['password']
        inputrpwd=total_cleaned_data['rpassword']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('should match with password')

        input_bot_handler=total_cleaned_data['bot_handler']
        if len(input_bot_handler)>0:
            raise forms.ValidationError('This request coming from Robot')
