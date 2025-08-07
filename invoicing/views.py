"""
Invoicing views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def invoice_list(request):
    """Invoice list view."""
    return render(request, 'invoicing/invoice-list.html', {})


@login_required
def invoice_details(request):
    """Invoice details view."""
    return render(request, 'invoicing/invoice-details.html', {})


@login_required
def create_invoice(request):
    """Create invoice view."""
    return render(request, 'invoicing/create-invoice.html', {})


@login_required
def edit_invoice(request):
    """Edit invoice view."""
    return render(request, 'invoicing/edit-invoice.html', {})
