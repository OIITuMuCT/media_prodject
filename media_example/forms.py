from django import forms

class ExampleForm(forms.Form):
    file_upload = forms.FileField()