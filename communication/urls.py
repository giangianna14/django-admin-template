"""
Communication URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('email/', views.inbox, name='email'),  # Alias for inbox
    path('calendar/', views.calendar, name='calendar'),
    path('to-do-list/', views.to_do_list, name='to-do-list'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts-2/', views.contacts_two, name='contacts-2'),
    path('chat/', views.chat, name='chat'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('read-email/', views.read_email, name='read-email'),
    path('snoozed/', views.snoozed, name='snoozed'),
    path('draft/', views.draft, name='draft'),
    path('sent-mail/', views.sent_mail, name='sent-mail'),
    path('trash-email/', views.trash_email, name='trash-email'),
    path('spam/', views.spam, name='spam'),
    path('starred/', views.starred, name='starred'),
    path('important/', views.important, name='important'),
]
