from django.urls import path

from .views import FileView, UploadFileView

app_name = 'api'

urlpatterns = [
    path('file/', FileView.as_view(), name='view_file'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
]
