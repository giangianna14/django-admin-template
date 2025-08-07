"""
File Management URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'file_management'

urlpatterns = [
    path('', views.file_manager, name='file-manager'),
    path('upload/', views.file_upload, name='file-upload'),
    path('assets/', views.assets, name='assets'),
    path('projects/', views.projects, name='projects'),
    path('personal/', views.personal, name='personal'),
    path('applications/', views.applications, name='applications'),
    path('documents/', views.documents, name='documents'),
    path('media/', views.media, name='media'),
    path('recents/', views.recents, name='recents'),
    path('important/', views.drive_important, name='drive-important'),
    path('spam/', views.drive_spam, name='drive-spam'),
    path('trash/', views.drive_trash, name='drive-trash'),
]
