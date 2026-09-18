"""
Menu Template Tags

Template tags for rendering dynamic menus in templates.
"""
from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse, NoReverseMatch
from ..models import MenuCategory, MenuItem, MenuSettings

register = template.Library()


@register.inclusion_tag('menu_management/menu_sidebar.html', takes_context=True)
def render_sidebar_menu(context):
    """Render the sidebar menu"""
    request = context['request']
    user = request.user
    
    # Get menu settings
    settings = MenuSettings.get_settings()
    
    # Get active categories with their menu items
    categories = MenuCategory.objects.filter(
        is_active=True
    ).prefetch_related(
        'menu_items__children'
    ).order_by('order')
    
    # Filter menu items by user permissions
    filtered_categories = []
    for category in categories:
        category_items = []
        
        # Get top-level menu items for this category
        top_level_items = category.menu_items.filter(
            parent__isnull=True,
            is_active=True
        ).order_by('order', 'title')
        
        for menu_item in top_level_items:
            if menu_item.can_user_access(user):
                # Get children for this menu item
                children = []
                for child in menu_item.get_children():
                    if child.can_user_access(user):
                        children.append(child)
                
                # Add menu item with filtered children
                menu_item.filtered_children = children
                category_items.append(menu_item)
        
        # Only include category if it has accessible items
        if category_items:
            category.filtered_items = category_items
            filtered_categories.append(category)
    
    return {
        'categories': filtered_categories,
        'settings': settings,
        'request': request,
        'user': user
    }


@register.inclusion_tag('menu_management/menu_horizontal.html', takes_context=True)
def render_horizontal_menu(context):
    """Render the horizontal menu"""
    request = context['request']
    user = request.user
    
    # Get menu settings
    settings = MenuSettings.get_settings()
    
    # Get active top-level menu items only
    menu_items = MenuItem.objects.filter(
        is_active=True,
        parent__isnull=True
    ).select_related('category').order_by('category__order', 'order', 'title')
    
    # Filter by user permissions
    filtered_items = []
    for menu_item in menu_items:
        if menu_item.can_user_access(user):
            # Get children for dropdowns
            children = []
            for child in menu_item.get_children():
                if child.can_user_access(user):
                    children.append(child)
            
            menu_item.filtered_children = children
            filtered_items.append(menu_item)
    
    return {
        'menu_items': filtered_items,
        'settings': settings,
        'request': request,
        'user': user
    }


@register.simple_tag(takes_context=True)
def is_menu_active(context, menu_item):
    """Check if a menu item should be marked as active"""
    request = context['request']
    current_path = request.path
    
    # Check direct URL match
    if menu_item.url_pattern:
        patterns = [p.strip() for p in menu_item.url_pattern.split(',')]
        for pattern in patterns:
            if pattern and current_path.startswith(pattern):
                return True
    
    # Check URL name match
    if menu_item.url_name:
        try:
            if menu_item.url_name.startswith('http'):
                # External URL
                return False
            
            resolved_url = reverse(menu_item.url_name)
            if current_path == resolved_url:
                return True
        except NoReverseMatch:
            pass
    
    # Check children for active state
    for child in menu_item.get_children():
        if is_menu_active(context, child):
            return True
    
    return False


@register.simple_tag(takes_context=True)
def get_menu_url(context, menu_item):
    """Get the URL for a menu item"""
    if not menu_item.url_name:
        return '#'
    
    try:
        if menu_item.url_name.startswith('http'):
            return menu_item.url_name
        return reverse(menu_item.url_name)
    except NoReverseMatch:
        return '#'


@register.simple_tag
def menu_icon(menu_item):
    """Render menu icon HTML"""
    return mark_safe(menu_item.get_icon_html())


@register.simple_tag
def menu_badge(menu_item, settings=None):
    """Render menu badge if exists and badges are enabled"""
    if not menu_item.badge_text:
        return ''
    
    if settings and not settings.show_menu_badges:
        return ''
    
    badge_class = menu_item.badge_class or 'hot tag'
    return mark_safe(f'<span class="{badge_class}">{menu_item.badge_text}</span>')


@register.filter
def has_children(menu_item):
    """Check if menu item has children"""
    return menu_item.has_children()


@register.simple_tag
def menu_settings():
    """Get menu settings"""
    return MenuSettings.get_settings()


@register.inclusion_tag('menu_management/breadcrumb.html', takes_context=True)
def render_breadcrumb(context, title=None):
    """Render breadcrumb navigation based on current menu"""
    request = context['request']
    current_path = request.path
    
    # Find current menu item
    current_menu = None
    breadcrumbs = []
    
    try:
        # Try to find menu item by URL pattern
        menu_items = MenuItem.objects.filter(
            is_active=True
        ).select_related('parent', 'category')
        
        for item in menu_items:
            if item.url_pattern and current_path.startswith(item.url_pattern):
                current_menu = item
                break
            elif item.url_name:
                try:
                    if not item.url_name.startswith('http'):
                        resolved_url = reverse(item.url_name)
                        if current_path == resolved_url:
                            current_menu = item
                            break
                except NoReverseMatch:
                    continue
        
        # Build breadcrumb trail
        if current_menu:
            # Add parents to breadcrumb
            menu = current_menu
            trail = []
            while menu:
                trail.insert(0, menu)
                menu = menu.parent
            
            breadcrumbs = trail
    
    except Exception:
        pass
    
    return {
        'breadcrumbs': breadcrumbs,
        'current_title': title,
        'request': request
    }


@register.simple_tag(takes_context=True)
def menu_count_by_category(context, category_type):
    """Get count of menu items by category type"""
    try:
        return MenuItem.objects.filter(
            category__category_type=category_type,
            is_active=True
        ).count()
    except:
        return 0


@register.simple_tag
def get_menu_by_slug(slug):
    """Get menu item by slug"""
    try:
        return MenuItem.objects.get(slug=slug, is_active=True)
    except MenuItem.DoesNotExist:
        return None


@register.inclusion_tag('menu_management/menu_item.html', takes_context=True)
def render_menu_item(context, menu_item, level=0):
    """Render a single menu item with its children"""
    request = context['request']
    user = request.user
    settings = context.get('settings') or MenuSettings.get_settings()
    
    # Check if user can access this menu
    if not menu_item.can_user_access(user):
        return {'render': False}
    
    # Get filtered children
    children = []
    for child in menu_item.get_children():
        if child.can_user_access(user):
            children.append(child)
    
    return {
        'render': True,
        'menu_item': menu_item,
        'children': children,
        'level': level,
        'settings': settings,
        'request': request,
        'is_active': is_menu_active(context, menu_item),
        'menu_url': get_menu_url(context, menu_item)
    }
