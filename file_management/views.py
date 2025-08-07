"""
File Management views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def file_manager(request):
    """File manager view."""
    return render(request, 'file_management/file-manager.html', {})


@login_required
def file_upload(request):
    """File upload view."""
    return render(request, 'file_management/file-upload.html', {})


@login_required
def assets(request):
    """Assets view."""
    return render(request, 'file_management/assets.html', {})


@login_required
def projects(request):
    """Projects files view."""
    return render(request, 'file_management/projects.html', {})


@login_required
def personal(request):
    """Personal files view."""
    return render(request, 'file_management/personal.html', {})


@login_required
def applications(request):
    """Applications view."""
    return render(request, 'file_management/applications.html', {})


@login_required
def documents(request):
    """Documents view."""
    return render(request, 'file_management/documents.html', {})


@login_required
def media(request):
    """Media files view."""
    return render(request, 'file_management/media.html', {})


@login_required
def recents(request):
    """Recent files view."""
    return render(request, 'file_management/recents.html', {})


@login_required
def drive_important(request):
    """Important files view."""
    return render(request, 'file_management/drive-important.html', {})


@login_required
def drive_spam(request):
    """Spam files view."""
    return render(request, 'file_management/drive-spam.html', {})


@login_required
def drive_trash(request):
    """Trash files view."""
    return render(request, 'file_management/drive-trash.html', {})
