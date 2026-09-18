"""
Menu Management URLs

URL patterns for menu management views.
"""
from django.urls import path
from . import views

app_name = 'menu_management'

urlpatterns = [
    # Dashboard
    path('', views.menu_dashboard, name='dashboard'),
    
    # Menu Categories
    path('categories/', views.MenuCategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.MenuCategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.MenuCategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.MenuCategoryDeleteView.as_view(), name='category_delete'),
    
    # Menu Items
    path('menus/', views.MenuItemListView.as_view(), name='menu_list'),
    path('menus/create/', views.MenuItemCreateView.as_view(), name='menu_create'),
    path('menus/<int:pk>/edit/', views.MenuItemUpdateView.as_view(), name='menu_edit'),
    path('menus/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menu_delete'),
    path('menus/<int:menu_id>/toggle-status/', views.toggle_menu_status, name='toggle_menu_status'),
    
    # Menu Organization
    path('reorder/', views.menu_reorder, name='menu_reorder'),
    path('preview/', views.menu_preview, name='menu_preview'),
    
    # Settings
    path('settings/', views.menu_settings, name='menu_settings'),
    
    # Logs
    path('logs/', views.menu_logs, name='menu_logs'),
]
