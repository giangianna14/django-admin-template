"""
Authentication URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forget-password/', views.forget_password, name='forget-password'),
    path('forgot-password/', views.forget_password, name='forgot-password'),  # Alias
    path('reset-password/', views.reset_password, name='reset-password'),
    path('lock-screen/', views.lock_screen, name='lock-screen'),
    path('logout/', views.logout, name='logout'),
    path('confirm-mail/', views.confirm_mail, name='confirm-mail'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('account-settings/', views.account_settings, name='account-settings'),
    path('change-password/', views.change_password, name='change-password'),
    path('connections/', views.connections, name='connections'),
]
