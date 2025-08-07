"""
Support URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('', views.help_desk, name='support'),  # Root support page
    path('help/', views.help_desk, name='help'),  # Help page
    path('tickets/', views.tickets, name='tickets'),
    path('ticket-details/', views.ticket_details, name='ticket-details'),
    path('agents/', views.agents, name='agents'),
    path('reports/', views.reports, name='reports'),
]
