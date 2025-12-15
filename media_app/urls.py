from django.urls import path
from .views import (GenerateUploadURLView,
                    MediaFileCreateView,
                    MediaFileListView,
                    )


urlpatterns = [
    path("generate-upload-url/", GenerateUploadURLView.as_view(),name="generate-upload-url"),
    path("files/", MediaFileListView.as_view(),name="get-files"),
    path("files/create/", MediaFileCreateView.as_view(),name="create-files"),
]

