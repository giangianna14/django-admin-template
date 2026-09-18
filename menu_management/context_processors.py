"""
Menu Management Context Processors

Provides menu-related context to all templates.
"""
from .models import MenuSettings


def menu_context(request):
    """
    Add menu settings and context to all templates.
    """
    try:
        settings = MenuSettings.get_settings()
        return {
            'menu_settings': settings,
        }
    except Exception:
        # Return default values if settings not available
        return {
            'menu_settings': {
                'site_name': 'Trezo',
                'logo_icon': '/static/images/logo-icon.png',
                'show_menu_icons': True,
                'show_menu_badges': True,
                'menu_style': 'sidebar',
            }
        }
