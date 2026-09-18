"""
Main URL configuration for the Django admin template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core pages (home, features, contact, etc.)
    path('', include('core.urls')),

    # Authentication (login, register, etc.) - must come before allauth
    path('auth/', include('authentication.urls')),

    # Redirect allauth account URLs to custom auth
    path('accounts/login/', RedirectView.as_view(url='/auth/login/', query_string=True)),
    path('accounts/signup/', RedirectView.as_view(url='/auth/register/', query_string=True)),
    path('accounts/logout/', RedirectView.as_view(url='/auth/logout/', query_string=True)),

    # Django-allauth URLs
    path('accounts/', include('allauth.urls')),
    
    # Dashboard pages
    path('dashboard/', include('dashboard.urls')),
    
    # Menu Management
    path('menu-management/', include('menu_management.urls')),
    
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

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
