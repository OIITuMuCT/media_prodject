"""
URL configuration for media_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import media_example.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", media_example.views.index, name="index"),
    path("media-example/", media_example.views.media_example, name="media_example"),
    path("view/", media_example.views.view, name="view"),
    path("success/", media_example.views.success, name="success-url"),
    path("my-view/", media_example.views.my_view),
    path("picture-form/", media_example.views.image_view, name="image_form"),
    path(
        "downloads/<path:relative_path>",
        media_example.views.download_view,
        name="downloads",
    ),
    path(
        "example-model/", media_example.views.view_example_model, name="example_model"
    ),
    path("db-view-1/", media_example.views.view_db_1, name="db-view-1"),
    path("db-view/", media_example.views.view_db, name="db-view"),
    path("image-file/", media_example.views.image_file_view, name="image-file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
