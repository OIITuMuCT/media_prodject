import pathlib
from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    file_field = models.FileField(upload_to=pathlib.Path("files/%Y/%m/%d"))