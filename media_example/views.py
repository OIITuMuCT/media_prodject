from django.shortcuts import render
from django.conf import settings
from myproject.myapp.models import Review

# Create your views here.
def my_view(request):
    return render(request, "template.html", {"MEDIA_URL":
        settings.MEDIA_URL, "username": "jbloggs"})

def media(request):
    """
    Add media-related context variables to the context.
    """
    return {"MEDIA_URL": settings.MEDIA_URL}


def latest_review(request):
    return {"latest_reviews": Review.objects.order_by("-date_created")[:5]}
