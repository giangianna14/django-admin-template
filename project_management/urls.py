"""
Project Management URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'project_management'

urlpatterns = [
    path('', views.project_overview, name='projects'),  # Root projects page
    path('kanban/', views.kanban_board, name='kanban'),  # Alias for kanban-board
    path('kanban-board/', views.kanban_board, name='kanban-board'),
    path('kanban-board-2/', views.kanban_board_two, name='kanban-board-2'),
    path('overview/', views.project_overview, name='project-overview'),
    path('list/', views.project_list, name='project-list'),
    path('create/', views.create_project, name='create-project'),
    path('clients/', views.clients, name='clients'),
    path('teams/', views.teams, name='teams'),
    path('teams-2/', views.teams_two, name='teams-2'),
    path('leads/', views.leads, name='leads'),
    path('deals/', views.deals, name='deals'),
]
