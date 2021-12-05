from django.urls import path

from . import views

app_name = 'admin-blog'

urlpatterns = [
    path('upload-image/', views.AdminUploadImageView.as_view(), name='admin-upload-image'),
]
