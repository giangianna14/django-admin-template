"""
Invoicing URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'invoicing'

urlpatterns = [
    path('', views.invoice_list, name='invoice-list'),
    path('list/', views.invoice_list, name='list'),  # Alias for invoice-list
    path('details/', views.invoice_details, name='invoice-details'),
    path('create/', views.create_invoice, name='create-invoice'),
    path('edit/', views.edit_invoice, name='edit-invoice'),
]
