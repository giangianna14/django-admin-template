"""
Core views for main pages like home, features, contact, etc.
"""
from django.shortcuts import render


def home(request):
    """Homepage view."""
    return render(request, 'core/home.html', {})


def features(request):
    """Features page view."""
    return render(request, 'core/features.html', {})


def our_team(request):
    """Our team page view."""
    return render(request, 'core/our-team.html', {})


def faqs(request):
    """FAQs page view."""
    return render(request, 'core/faqs.html', {})


def contact(request):
    """Contact page view."""
    return render(request, 'core/contact.html', {})


def faq(request):
    """Single FAQ page view."""
    return render(request, 'core/faq.html', {})


def pricing_plan(request):
    """Pricing plan page view."""
    return render(request, 'core/pricing-plan.html', {})


def timeline(request):
    """Timeline page view."""
    return render(request, 'core/timeline.html', {})


def gallery(request):
    """Gallery page view."""
    return render(request, 'core/gallery.html', {})


def search(request):
    """Search page view."""
    return render(request, 'core/search.html', {})


def blank_page(request):
    """Blank page view."""
    return render(request, 'core/blank-page.html', {})


def error_page(request):
    """Error page view."""
    return render(request, 'core/error-page.html', {})


def internal_error(request):
    """Internal error page view."""
    return render(request, 'core/internal-error.html', {})


def widgets(request):
    """Widgets page view."""
    return render(request, 'core/widgets.html', {})


def google_map(request):
    """Google map page view."""
    return render(request, 'core/google-map.html', {})


def notification(request):
    """Notification page view."""
    return render(request, 'core/notification.html', {})


def privacy_policy(request):
    """Privacy policy page view."""
    return render(request, 'core/privacy-policy.html', {})


def terms_conditions(request):
    """Terms and conditions page view."""
    return render(request, 'core/terms-conditions.html', {})
