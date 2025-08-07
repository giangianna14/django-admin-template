"""
UI Components views for various UI elements and components.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def alerts(request):
    """Alerts component view."""
    return render(request, 'ui_components/alerts.html', {})


@login_required
def avatar(request):
    """Avatar component view."""
    return render(request, 'ui_components/avatar.html', {})


@login_required
def buttons(request):
    """Buttons component view."""
    return render(request, 'ui_components/buttons.html', {})


@login_required
def badges(request):
    """Badges component view."""
    return render(request, 'ui_components/badges.html', {})


@login_required
def cards(request):
    """Cards component view."""
    return render(request, 'ui_components/cards.html', {})


@login_required
def carousels(request):
    """Carousels component view."""
    return render(request, 'ui_components/carousels.html', {})


@login_required
def dropdowns(request):
    """Dropdowns component view."""
    return render(request, 'ui_components/dropdowns.html', {})


@login_required
def grids(request):
    """Grids component view."""
    return render(request, 'ui_components/grids.html', {})


@login_required
def images(request):
    """Images component view."""
    return render(request, 'ui_components/images.html', {})


@login_required
def list(request):
    """List component view."""
    return render(request, 'ui_components/list.html', {})


@login_required
def modals(request):
    """Modals component view."""
    return render(request, 'ui_components/modals.html', {})


@login_required
def navs(request):
    """Navigation component view."""
    return render(request, 'ui_components/navs.html', {})


@login_required
def paginations(request):
    """Pagination component view."""
    return render(request, 'ui_components/paginations.html', {})


@login_required
def popover_tooltips(request):
    """Popover tooltips component view."""
    return render(request, 'ui_components/popover-tooltips.html', {})


@login_required
def progress(request):
    """Progress component view."""
    return render(request, 'ui_components/progress.html', {})


@login_required
def spinners(request):
    """Spinners component view."""
    return render(request, 'ui_components/spinners.html', {})


@login_required
def tabs(request):
    """Tabs component view."""
    return render(request, 'ui_components/tabs.html', {})


@login_required
def accordions(request):
    """Accordions component view."""
    return render(request, 'ui_components/accordions.html', {})


@login_required
def typography(request):
    """Typography component view."""
    return render(request, 'ui_components/typography.html', {})


@login_required
def sweet_alarts(request):
    """Sweet alerts component view."""
    return render(request, 'ui_components/sweet-alarts.html', {})


@login_required
def animation(request):
    """Animation component view."""
    return render(request, 'ui_components/animation.html', {})


@login_required
def clip_board(request):
    """Clipboard component view."""
    return render(request, 'ui_components/clip-board.html', {})


@login_required
def drag_drop(request):
    """Drag & Drop component view."""
    return render(request, 'ui_components/drag-drop.html', {})


@login_required
def range_slider(request):
    """Range slider component view."""
    return render(request, 'ui_components/range-slider.html', {})


@login_required
def ratings(request):
    """Ratings component view."""
    return render(request, 'ui_components/ratings.html', {})


@login_required
def toasts(request):
    """Toasts component view."""
    return render(request, 'ui_components/toasts.html', {})


@login_required
def check_radio(request):
    """Checkbox & Radio component view."""
    return render(request, 'ui_components/check-radio.html', {})


@login_required
def select(request):
    """Select component view."""
    return render(request, 'ui_components/select.html', {})


@login_required
def scrollbar(request):
    """Scrollbar component view."""
    return render(request, 'ui_components/scrollbar.html', {})
