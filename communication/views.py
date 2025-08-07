"""
Communication views for email, chat, calendar, etc.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def calendar(request):
    """Calendar view."""
    return render(request, 'communication/calendar.html', {})


@login_required
def to_do_list(request):
    """To-do list view."""
    return render(request, 'communication/to-do-list.html', {})


@login_required
def contacts(request):
    """Contacts list view."""
    return render(request, 'communication/contacts.html', {})


@login_required
def contacts_two(request):
    """Alternative contacts view."""
    return render(request, 'communication/contacts-2.html', {})


@login_required
def chat(request):
    """Chat view."""
    return render(request, 'communication/chat.html', {})


@login_required
def inbox(request):
    """Email inbox view."""
    return render(request, 'communication/inbox.html', {})


@login_required
def compose(request):
    """Compose email view."""
    return render(request, 'communication/compose.html', {})


@login_required
def read_email(request):
    """Read email view."""
    return render(request, 'communication/read-email.html', {})


@login_required
def snoozed(request):
    """Snoozed emails view."""
    return render(request, 'communication/snoozed.html', {})


@login_required
def draft(request):
    """Draft emails view."""
    return render(request, 'communication/draft.html', {})


@login_required
def sent_mail(request):
    """Sent emails view."""
    return render(request, 'communication/sent-mail.html', {})


@login_required
def trash_email(request):
    """Trash emails view."""
    return render(request, 'communication/trash-email.html', {})


@login_required
def spam(request):
    """Spam emails view."""
    return render(request, 'communication/spam.html', {})


@login_required
def starred(request):
    """Starred emails view."""
    return render(request, 'communication/starred.html', {})


@login_required
def important(request):
    """Important emails view."""
    return render(request, 'communication/important.html', {})
