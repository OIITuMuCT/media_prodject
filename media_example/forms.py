from django import forms

class ExampleForm(forms.Form):

    file_upload = forms.FileField()


class UploadForm(forms.Form):
    file_upload = forms.FileField()


class PictureForm(forms.Form):
    picture = forms.ImageField()

class ImageFileForm(forms.Form):
    image_upload = forms.ImageField()
    file_upload = forms.FileField()