import pathlib
from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    file_field = models.FileField(upload_to=pathlib.Path("files/%Y/%m/%d"))
    
    # image = models.ImageField(upload_to="images/%Y/%m/%d/",
    #                           height_field="image_height",
    #                           width_field="image_width"
    #                         )
    # image_height = models.IntegerField()
    # image_width = models.IntegerField()