"""
Dashboard URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.ecommerce, name='ecommerce'),
    path('crm/', views.crm, name='crm'),
    path('project-management/', views.project_management, name='project-management'),
    path('lms/', views.lms, name='lms'),
    path('help-desk/', views.help_desk, name='help-desk'),
    path('analytics/', views.analytics, name='analytics'),
    path('crypto/', views.crypto, name='crypto'),
    path('sales/', views.sales, name='sales'),
    path('hospital/', views.hospital, name='hospital'),
    path('marketing/', views.marketing, name='marketing'),
    path('nft/', views.nft, name='nft'),
    path('saas/', views.saas, name='saas'),
    path('real-estate/', views.real_estate, name='real-estate'),
    path('shipment/', views.shipment, name='shipment'),
    path('finance/', views.finance, name='finance'),
    path('hrm/', views.hrm, name='hrm'),
    path('school/', views.school, name='school'),
    path('call-center/', views.call_center, name='call-center'),
    path('pos-system/', views.pos_system, name='pos-system'),
    path('podcast/', views.podcast, name='podcast'),
    path('social-media/', views.social_media, name='social-media'),
]
