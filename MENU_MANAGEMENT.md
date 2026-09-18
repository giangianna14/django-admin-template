# Menu Management System

A comprehensive Django-based menu management system that allows dynamic creation, editing, and organization of navigation menus.

## Features

### 🎯 Core Features
- **Dynamic Menu Creation**: Create and manage menus through admin interface or web UI
- **Hierarchical Structure**: Support for nested menus (dropdowns, sub-menus)
- **Permission-Based Access**: Control menu visibility based on user permissions and groups
- **Multiple Menu Types**: Link menus, dropdown menus, and separators
- **Icon Support**: Material Icons, Feather Icons, and custom icon support
- **Badge System**: Add badges (Hot, New, etc.) to menu items
- **Menu Categories**: Organize menus into categories (MAIN, APPS, PAGES, MODULES, OTHERS)

### 🔧 Management Features
- **Web-based Dashboard**: Comprehensive menu management interface
- **Drag & Drop Reordering**: Easily reorder menu items
- **Bulk Operations**: Activate/deactivate multiple menu items
- **Menu Preview**: Preview menu structure before publishing
- **Import/Export**: Import and export menu configurations
- **Change Logs**: Track all menu changes with audit logging

### 🎨 Customization
- **Theme Support**: Multiple menu styles (sidebar, horizontal, mixed)
- **Custom CSS/JS**: Add custom styling and behavior
- **Responsive Design**: Mobile-friendly menu layouts
- **Brand Customization**: Custom logos, site names, and colors

## Installation

### 1. Add to Django Settings

```python
INSTALLED_APPS = [
    # ... other apps
    'menu_management',
]

# Add context processor
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ... other processors
                'menu_management.context_processors.menu_context',
            ],
        },
    },
]
```

### 2. Add URLs

```python
# urls.py
urlpatterns = [
    # ... other URLs
    path('menu-management/', include('menu_management.urls')),
]
```

### 3. Run Migrations

```bash
python manage.py makemigrations menu_management
python manage.py migrate
```

### 4. Populate Initial Data

```bash
python manage.py populate_menus
```

## Usage

### Admin Interface

1. **Access Django Admin**: `/admin/`
2. **Menu Management Section**: 
   - Menu Categories
   - Menu Items
   - Menu Settings
   - Menu Logs

### Web Interface

1. **Menu Dashboard**: `/menu-management/`
2. **Create Categories**: `/menu-management/categories/create/`
3. **Create Menu Items**: `/menu-management/menus/create/`
4. **Reorder Menus**: `/menu-management/reorder/`
5. **Menu Settings**: `/menu-management/settings/`

### Template Usage

#### Dynamic Sidebar
```html
{% load menu_tags %}
{% render_sidebar_menu %}
```

#### Horizontal Menu
```html
{% load menu_tags %}
{% render_horizontal_menu %}
```

#### Custom Menu Rendering
```html
{% load menu_tags %}
{% for category in categories %}
    <h3>{{ category.name }}</h3>
    {% for menu_item in category.filtered_items %}
        {% render_menu_item menu_item %}
    {% endfor %}
{% endfor %}
```

## Models

### MenuCategory
- **name**: Category display name
- **slug**: URL-friendly identifier
- **category_type**: Type (main, apps, pages, modules, others)
- **order**: Display order
- **is_active**: Active status

### MenuItem
- **title**: Menu item title
- **slug**: URL-friendly identifier
- **url_name**: Django URL name or absolute URL
- **url_pattern**: Pattern for active state checking
- **parent**: Parent menu item (for hierarchy)
- **category**: Menu category
- **menu_type**: Type (link, dropdown, separator)
- **icon**: Icon class/name
- **badge_text**: Badge text (Hot, New, etc.)
- **order**: Display order
- **permissions**: Required permissions and groups
- **is_active**: Active status

### MenuSettings
- **site_name**: Site name for branding
- **logo_icon**: Logo image path
- **menu_style**: Menu layout style
- **show_menu_icons**: Toggle icon display
- **show_menu_badges**: Toggle badge display
- **custom_css**: Custom CSS styling
- **custom_js**: Custom JavaScript

## Template Tags

### Core Tags
- `{% render_sidebar_menu %}`: Render sidebar menu
- `{% render_horizontal_menu %}`: Render horizontal menu
- `{% menu_settings %}`: Get menu settings
- `{% is_menu_active menu_item %}`: Check if menu is active
- `{% get_menu_url menu_item %}`: Get menu item URL
- `{% menu_icon menu_item %}`: Render menu icon
- `{% menu_badge menu_item %}`: Render menu badge

### Utility Tags
- `{% menu_count_by_category category_type %}`: Count menus by category
- `{% get_menu_by_slug slug %}`: Get menu item by slug
- `{% render_breadcrumb %}`: Render breadcrumb navigation

## Management Commands

### populate_menus
Populate menu system with initial data from existing sidebar structure.

```bash
# Populate with existing data
python manage.py populate_menus

# Reset and populate
python manage.py populate_menus --reset
```

## Permissions

### Required Permissions
- `menu_management.view_menucategory`: View categories
- `menu_management.add_menucategory`: Create categories
- `menu_management.change_menucategory`: Edit categories
- `menu_management.delete_menucategory`: Delete categories
- `menu_management.view_menuitem`: View menu items
- `menu_management.add_menuitem`: Create menu items
- `menu_management.change_menuitem`: Edit menu items
- `menu_management.delete_menuitem`: Delete menu items
- `menu_management.view_menusettings`: View settings
- `menu_management.change_menusettings`: Change settings

### User Groups
- **Menu Administrators**: Full access to all menu management features
- **Menu Editors**: Create and edit menu items
- **Menu Viewers**: View-only access to menu management

## API Endpoints

### Categories
- `GET /menu-management/categories/`: List categories
- `POST /menu-management/categories/create/`: Create category
- `PUT /menu-management/categories/<id>/edit/`: Update category
- `DELETE /menu-management/categories/<id>/delete/`: Delete category

### Menu Items
- `GET /menu-management/menus/`: List menu items
- `POST /menu-management/menus/create/`: Create menu item
- `PUT /menu-management/menus/<id>/edit/`: Update menu item
- `DELETE /menu-management/menus/<id>/delete/`: Delete menu item
- `POST /menu-management/menus/<id>/toggle-status/`: Toggle active status

### Utilities
- `GET /menu-management/reorder/`: Reorder interface
- `POST /menu-management/reorder/`: Update menu order
- `GET /menu-management/preview/`: Preview menu structure
- `GET /menu-management/settings/`: Menu settings
- `POST /menu-management/settings/`: Update settings

## Configuration

### Settings Variables
```python
# Menu cache timeout (seconds)
MENU_CACHE_TIMEOUT = 3600

# Maximum menu nesting depth
MENU_MAX_DEPTH = 3

# Media files for logo uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### CSS Classes
The system uses Bootstrap-compatible CSS classes:
- `menu-item`: Menu item container
- `menu-link`: Menu link element
- `menu-icon`: Menu icon container
- `menu-sub`: Submenu container
- `active`: Active menu state
- `open`: Open dropdown state

## Best Practices

### Menu Structure
1. **Limit Nesting**: Keep menu hierarchy shallow (max 3 levels)
2. **Logical Grouping**: Group related items in categories
3. **Clear Naming**: Use descriptive, concise menu titles
4. **Consistent Icons**: Use consistent icon style throughout

### Performance
1. **Caching**: Enable menu caching for better performance
2. **Lazy Loading**: Load submenu content on demand
3. **Minimal Queries**: Use select_related and prefetch_related
4. **Icon Optimization**: Optimize icon assets for fast loading

### Security
1. **Permission Checks**: Always check user permissions
2. **Input Validation**: Validate all menu data inputs
3. **XSS Prevention**: Sanitize menu content
4. **Access Control**: Restrict menu management to authorized users

## Troubleshooting

### Common Issues

#### Menu Not Displaying
1. Check if menu items are active
2. Verify user permissions
3. Ensure template tags are loaded
4. Check category assignments

#### Icons Not Showing
1. Verify icon library is loaded
2. Check icon names/classes
3. Ensure icon type is correct
4. Validate CSS inclusion

#### URL Errors
1. Check URL name validity
2. Verify URL patterns
3. Ensure namespace inclusion
4. Test URL reversing

### Debug Mode
Enable debug logging for menu system:

```python
LOGGING = {
    'loggers': {
        'menu_management': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit pull request

## License

This menu management system is part of the Django Admin Template project and follows the same licensing terms.

## Support

For support and questions:
- Create an issue in the project repository
- Check documentation and examples
- Review existing menu configurations
- Test with minimal configuration first
