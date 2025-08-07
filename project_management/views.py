"""
Project Management views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def kanban_board(request):
    """Kanban board view."""
    return render(request, 'project_management/kanban-board.html', {})


@login_required
def kanban_board_two(request):
    """Alternative kanban board view."""
    return render(request, 'project_management/kanban-board-2.html', {})


@login_required
def project_overview(request):
    """Project overview view."""
    return render(request, 'project_management/project-overview.html', {})


@login_required
def project_list(request):
    """Project list view."""
    return render(request, 'project_management/project-list.html', {})


@login_required
def create_project(request):
    """Create project view."""
    return render(request, 'project_management/create-project.html', {})


@login_required
def clients(request):
    """Clients view."""
    return render(request, 'project_management/clients.html', {})


@login_required
def teams(request):
    """Teams view."""
    return render(request, 'project_management/teams.html', {})


@login_required
def teams_two(request):
    """Alternative teams view."""
    return render(request, 'project_management/teams-2.html', {})


@login_required
def leads(request):
    """Leads view."""
    return render(request, 'project_management/leads.html', {})


@login_required
def deals(request):
    """Deals view."""
    return render(request, 'project_management/deals.html', {})
