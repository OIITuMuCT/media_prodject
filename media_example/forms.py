from django import forms

class ExampleForm(forms.Form):
    file_upload = forms.FileField()

class UploadForm(forms.Form):
    file_upload = forms.FileField()


class PictureForm(forms.Form):
    picture = forms.ImageField()
