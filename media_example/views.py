import os.path
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from PIL import Image
from .forms import ExampleForm, UploadForm, PictureForm, ImageFileForm, ImageFileModelForm
from .models import ExampleModel, ImageFileModel


# Create your views here.

def index(request):
    return render(request, "index.html")

def my_view(request):
    return render(
        request,
        "template.html",
        {"MEDIA_URL": settings.MEDIA_URL, "username": "jbloggs"},
    )


def media(request):
    """
    Add media-related context variables to the context.
    """
    return {"MEDIA_URL": settings.MEDIA_URL}


def media_example(request):
    if request.method == "POST":
        save_path = settings.MEDIA_ROOT / request.FILES["file_upload"].name

        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["file_upload"].chunks():
                output_file.write(chunk)
    return render(request, "media-example.html")


def view(request):
    if request.method == "POST":
        # instantiate the form with POST data and files
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            # process the form and save files
            save_path = settings.MEDIA_ROOT / request.FILES["file_upload"].name

            with open(save_path, "wb") as output_file:
                for chunk in request.FILES["file_upload"].chunks():
                    output_file.write(chunk)
            return redirect("success-url")
    else:
        # instantiate an empty form ad we've seen before
        form = ExampleForm()
    # render a template, the same as for other forms
    return render(request, "template.html", {"form": form})


def view_upload(request):
    form = UploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            save_path = os.path.join(
                settings.MEDIA_ROOT, request.FILES["file_upload"].name
            )
        
            with open(save_path, "wb") as output_file:
                for chunk in form.cleaned_data["file_upload"].chunks():
                    output_file.write(chunk)
    else:
        form = UploadForm()
    return render(request, "media-example.html", {"form": form})

def image_view(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = settings.MEDIA_ROOT / form.cleaned_data["picture"].name

            image = Image.open(form.cleaned_data["picture"])
            image.thumbnail((50, 50))
            image.save(save_path)

    else:
        form = PictureForm()
    return render(request, "picture-form.html")

def success(request):
    # return HttpResponse("Successfully upload file")
    return render(request, "success.html")

def download_view(request, relative_path):
    if request.user.is_anonymous:
        raise PermissionDenied
    full_path = os.path.join(settings.MEDIA_ROOT, "protected", relative_path)
    file_handle = open(full_path, "rb")
    return FileResponse(file_handle) # Django sends the file then closes the handle

def view_example_model(request):
    if request.method == "POST":
        m = ExampleModel() # Create a new ExampleModel instance
        if m == "image":
            m.image_filed = request.FILES["file_upload"]
            m.save()
        else:
            m.file_field = request.FILES["file_upload"]
            m.save()
    return render(request, "example-model.html")

def view_db(request):
    if request.method == "POST":
        form = ImageFileModelForm(request.POST, request.FILES)
        form.save()
        return redirect("success-url")
    else:
        form = ImageFileModelForm()
        
    return render(request, "db-view.html", {"form": form})

def image_file_view(request):
    instance = None
    if request.method == "POST":
        form = ImageFileForm(request.POST, request.FILES)

        if form.is_valid():

            instance = ImageFileModel()
            instance.image_field = form.cleaned_data["image_upload"]
            instance.file_field = form.cleaned_data["file_upload"]
            instance.save()
    else:
        form = ImageFileForm()
    return render(request, "image_file.html", {"form": form , "instance": instance})

def view_db_1(request):
    instance = None
    if request.method == "POST":
        form = ImageFileModelForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save()
    else:
        form = ImageFileModelForm()
    return render(request, "db-view-1.html", {"form": form, "instance": instance})