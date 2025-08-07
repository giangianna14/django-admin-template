"""
User Management views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_roles(request):
    """User roles management view."""
    return render(request, 'user_management/user-roles.html', {})


@login_required
def team_members(request):
    """Team members view."""
    return render(request, 'user_management/team-members.html', {})


@login_required
def users_list(request):
    """Users list view."""
    return render(request, 'user_management/users-list.html', {})


@login_required
def add_user(request):
    """Add user view."""
    return render(request, 'user_management/add-user.html', {})


@login_required
def user_profile(request):
    """User profile view."""
    return render(request, 'user_management/user-profile.html', {})


@login_required
def user(request):
    """User details view."""
    return render(request, 'user_management/user.html', {})


@login_required
def my_profile(request):
    """My profile view."""
    return render(request, 'user_management/my-profile.html', {})


@login_required
def my_projects(request):
    """My projects view."""
    return render(request, 'user_management/my-projects.html', {})


@login_required
def members(request):
    """Members view."""
    return render(request, 'user_management/members.html', {})
