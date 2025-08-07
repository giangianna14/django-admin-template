"""
Support & Help Desk views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def help_desk(request):
    """Help desk main view."""
    return render(request, 'support/help-desk.html', {})


@login_required
def tickets(request):
    """Tickets list view."""
    return render(request, 'support/tickets.html', {})


@login_required
def ticket_details(request):
    """Ticket details view."""
    return render(request, 'support/ticket-details.html', {})


@login_required
def agents(request):
    """Support agents view."""
    return render(request, 'support/agents.html', {})


@login_required
def reports(request):
    """Support reports view."""
    return render(request, 'support/reports.html', {})
