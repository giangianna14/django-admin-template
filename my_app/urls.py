"""
Main URL configuration for the Django admin template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Django-allauth URLs
    path('accounts/', include('allauth.urls')),
    
    # Core pages (home, features, contact, etc.)
    path('', include('core.urls')),
    
    # Authentication (login, register, etc.)
    path('auth/', include('authentication.urls')),
    
    # Dashboard pages
    path('dashboard/', include('dashboard.urls')),
    
    # E-commerce module
    path('ecommerce/', include('ecommerce.urls')),
    
    # Communication module (email, chat, calendar)
    path('communication/', include('communication.urls')),
    
    # UI Components
    path('components/', include('ui_components.urls')),
    
    # Learning Management System
    path('lms/', include('lms.urls')),
    
    # Events Management
    path('events/', include('events.urls')),
    
    # Invoicing
    path('invoicing/', include('invoicing.urls')),
    
    # Support & Help Desk
    path('support/', include('support.urls')),
    
    # User Management
    path('users/', include('user_management.urls')),
    
    # Project Management
    path('projects/', include('project_management.urls')),
    
    # File Management
    path('files/', include('file_management.urls')),
]

urlpatterns += staticfiles_urlpatterns()
