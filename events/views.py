"""
Events management views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def events(request):
    """Events calendar view."""
    return render(request, 'events/events.html', {})


@login_required
def events_list(request):
    """Events list view."""
    return render(request, 'events/events-list.html', {})


@login_required
def event_details(request):
    """Event details view."""
    return render(request, 'events/event-details.html', {})


@login_required
def create_an_event(request):
    """Create event view."""
    return render(request, 'events/create-an-event.html', {})


@login_required
def edit_an_event(request):
    """Edit event view."""
    return render(request, 'events/edit-an-event.html', {})


@login_required
def calendar(request):
    """Calendar view."""
    return render(request, 'events/calendar.html', {})
