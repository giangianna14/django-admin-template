"""
LMS URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'lms'

urlpatterns = [
    path('courses/', views.courses_list, name='courses-list'),
    path('course-details/', views.course_details, name='course-details'),
    path('lesson-preview/', views.lesson_preview, name='lesson-preview'),
    path('create-course/', views.create_course, name='create-course'),
    path('edit-course/', views.edit_course, name='edit-course'),
    path('instructors/', views.instructors, name='instructors'),
    path('students/', views.students, name='students'),
]
