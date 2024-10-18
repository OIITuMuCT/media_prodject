from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
# from myproject.myapp.models import Review
from .forms import ExampleForm

# Create your views here.
def my_view(request):
    return render(request, "template.html", {"MEDIA_URL":
        settings.MEDIA_URL, "username": "jbloggs"})

def media(request):
    """
    Add media-related context variables to the context.
    """
    return {"MEDIA_URL": settings.MEDIA_URL}


# def latest_review(request):
#     return {"latest_reviews": Review.objects.order_by("-date_created")[:5]}


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

        # TODO Нужно проработать эти два варианта
        # if form.is_valid():
        #     save_file_upload("/path/to/save.jpg",
        #     request.FILES["file_upload"])
        #     return redirect("/success-url/")
        # TODO Нужно проработать эти два варианта
        # if form.is_valid():
        #     save_file_upload("/path/to/save.jpg",
        #         form.cleaned_data["file_upload"])
        #     return redirect("/success-url/")

    else:
        # instantiate an empty form ad we've seen before
        form = ExampleForm()
    # render a template, the same as for other forms
    return render(request, "template.html", {"form": form})

def success(request):
    return HttpResponse("Successfully upload file")
