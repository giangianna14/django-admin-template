"""
User Management URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('', views.users_list, name='users'),  # Root users page
    path('roles/', views.user_roles, name='roles'),  # User roles
    path('team-members/', views.team_members, name='team-members'),
    path('list/', views.users_list, name='users-list'),
    path('add/', views.add_user, name='add-user'),
    path('profile/', views.user_profile, name='user-profile'),
    path('details/', views.user, name='user'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('my-projects/', views.my_projects, name='my-projects'),
    path('members/', views.members, name='members'),
]
