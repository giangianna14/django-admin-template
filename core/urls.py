"""
Core URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('our-team/', views.our_team, name='our-team'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('pricing-plan/', views.pricing_plan, name='pricing-plan'),
    path('timeline/', views.timeline, name='timeline'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search, name='search'),
    path('blank-page/', views.blank_page, name='blank-page'),
    path('error-page/', views.error_page, name='error-page'),
    path('internal-error/', views.internal_error, name='internal-error'),
    path('widgets/', views.widgets, name='widgets'),
    path('google-map/', views.google_map, name='google-map'),
    path('notification/', views.notification, name='notification'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-conditions/', views.terms_conditions, name='terms-conditions'),
]
