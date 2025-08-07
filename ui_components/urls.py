"""
UI Components URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'ui_components'

urlpatterns = [
    path('alerts/', views.alerts, name='alerts'),
    path('avatar/', views.avatar, name='avatar'),
    path('buttons/', views.buttons, name='buttons'),
    path('badges/', views.badges, name='badges'),
    path('cards/', views.cards, name='cards'),
    path('carousels/', views.carousels, name='carousels'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('grids/', views.grids, name='grids'),
    path('images/', views.images, name='images'),
    path('list/', views.list, name='list'),
    path('modals/', views.modals, name='modals'),
    path('navs/', views.navs, name='navs'),
    path('paginations/', views.paginations, name='paginations'),
    path('popover-tooltips/', views.popover_tooltips, name='popover-tooltips'),
    path('progress/', views.progress, name='progress'),
    path('spinners/', views.spinners, name='spinners'),
    path('tabs/', views.tabs, name='tabs'),
    path('accordions/', views.accordions, name='accordions'),
    path('typography/', views.typography, name='typography'),
    path('sweet-alarts/', views.sweet_alarts, name='sweet-alarts'),
    path('animation/', views.animation, name='animation'),
    path('clip-board/', views.clip_board, name='clip-board'),
    path('drag-drop/', views.drag_drop, name='drag-drop'),
    path('range-slider/', views.range_slider, name='range-slider'),
    path('ratings/', views.ratings, name='ratings'),
    path('toasts/', views.toasts, name='toasts'),
    path('check-radio/', views.check_radio, name='check-radio'),
    path('select/', views.select, name='select'),
    path('scrollbar/', views.scrollbar, name='scrollbar'),
]
