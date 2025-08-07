"""
Events URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='events'),
    path('list/', views.events_list, name='events-list'),
    path('details/', views.event_details, name='event-details'),
    path('create/', views.create_an_event, name='create-an-event'),
    path('edit/', views.edit_an_event, name='edit-an-event'),
    path('calendar/', views.calendar, name='calendar'),
]
