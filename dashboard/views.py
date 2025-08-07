"""
Dashboard views for various dashboard types.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def ecommerce(request):
    """E-commerce dashboard view."""
    return render(request, 'dashboard/ecommerce.html', {})


@login_required
def crm(request):
    """CRM dashboard view."""
    return render(request, 'dashboard/crm.html', {})


@login_required
def project_management(request):
    """Project management dashboard view."""
    return render(request, 'dashboard/project-management.html', {})


@login_required
def lms(request):
    """LMS dashboard view."""
    return render(request, 'dashboard/lms.html', {})


@login_required
def help_desk(request):
    """Help desk dashboard view."""
    return render(request, 'dashboard/help-desk.html', {})


@login_required
def analytics(request):
    """Analytics dashboard view."""
    return render(request, 'dashboard/analytics.html', {})


@login_required
def crypto(request):
    """Crypto dashboard view."""
    return render(request, 'dashboard/crypto.html', {})


@login_required
def sales(request):
    """Sales dashboard view."""
    return render(request, 'dashboard/sales.html', {})


@login_required
def hospital(request):
    """Hospital dashboard view."""
    return render(request, 'dashboard/hospital.html', {})


@login_required
def marketing(request):
    """Marketing dashboard view."""
    return render(request, 'dashboard/marketing.html', {})


@login_required
def nft(request):
    """NFT dashboard view."""
    return render(request, 'dashboard/nft.html', {})


@login_required
def saas(request):
    """SaaS dashboard view."""
    return render(request, 'dashboard/saas.html', {})


@login_required
def real_estate(request):
    """Real estate dashboard view."""
    return render(request, 'dashboard/real-estate.html', {})


@login_required
def shipment(request):
    """Shipment dashboard view."""
    return render(request, 'dashboard/shipment.html', {})


@login_required
def finance(request):
    """Finance dashboard view."""
    return render(request, 'dashboard/finance.html', {})


@login_required
def hrm(request):
    """HRM dashboard view."""
    return render(request, 'dashboard/hrm.html', {})


@login_required
def school(request):
    """School dashboard view."""
    return render(request, 'dashboard/school.html', {})


@login_required
def call_center(request):
    """Call center dashboard view."""
    return render(request, 'dashboard/call-center.html', {})


@login_required
def pos_system(request):
    """POS system dashboard view."""
    return render(request, 'dashboard/pos-system.html', {})


@login_required
def podcast(request):
    """Podcast dashboard view."""
    return render(request, 'dashboard/podcast.html', {})


@login_required
def social_media(request):
    """Social media dashboard view."""
    return render(request, 'dashboard/social-media.html', {})
