"""
LMS (Learning Management System) views.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def courses_list(request):
    """Courses list view."""
    return render(request, 'lms/courses-list.html', {})


@login_required
def course_details(request):
    """Course details view."""
    return render(request, 'lms/course-details.html', {})


@login_required
def lesson_preview(request):
    """Lesson preview view."""
    return render(request, 'lms/lesson-preview.html', {})


@login_required
def create_course(request):
    """Create course view."""
    return render(request, 'lms/create-course.html', {})


@login_required
def edit_course(request):
    """Edit course view."""
    return render(request, 'lms/edit-course.html', {})


@login_required
def instructors(request):
    """Instructors view."""
    return render(request, 'lms/instructors.html', {})


@login_required
def students(request):
    """Students view."""
    return render(request, 'lms/students.html', {})
