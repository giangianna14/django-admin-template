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
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset-password'),
    path('lock-screen/', views.lock_screen, name='lock-screen'),
    path('logout/', views.logout, name='logout'),
    path('confirm-mail/', views.confirm_mail, name='confirm-mail'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('account-settings/', views.account_settings, name='account-settings'),
    path('change-password/', views.change_password, name='change-password'),
    path('connections/', views.connections, name='connections'),
    
    # New password reset URLs
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/complete/', views.password_reset_complete, name='password_reset_complete'),
    
    # Test URL
    path('test-login/', views.test_login, name='test_login'),
]
