"""
Menu Management Models

This module contains models for managing dynamic menus and navigation.
Allows administrators to create, edit, and organize menu items dynamically.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse


class MenuCategory(models.Model):
    """
    Menu categories to group menu items (e.g., MAIN, APPS, PAGES, MODULES, OTHERS)
    """
    CATEGORY_TYPES = [
        ('main', 'MAIN'),
        ('apps', 'APPS'),
        ('pages', 'PAGES'),
        ('modules', 'MODULES'),
        ('others', 'OTHERS'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Category Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Category Slug")
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES, default='main')
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"
    
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Individual menu items with hierarchical structure support
    """
    MENU_TYPES = [
        ('link', 'Direct Link'),
        ('dropdown', 'Dropdown Menu'),
        ('separator', 'Separator'),
    ]
    
    ICON_TYPES = [
        ('material', 'Material Icons'),
        ('feather', 'Feather Icons'),
        ('custom', 'Custom Icon'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Menu Title")
    slug = models.SlugField(max_length=200, verbose_name="Menu Slug")
    url_name = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        help_text="Django URL name or absolute URL",
        verbose_name="URL Name"
    )
    url_pattern = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL pattern for active state checking",
        verbose_name="URL Pattern"
    )
    
    # Hierarchy
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        related_name='children',
        verbose_name="Parent Menu"
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name="Menu Category"
    )
    
    # Display properties
    menu_type = models.CharField(max_length=20, choices=MENU_TYPES, default='link')
    icon_type = models.CharField(max_length=20, choices=ICON_TYPES, default='material')
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon class or name (e.g., 'dashboard', 'shopping_cart')",
        verbose_name="Icon"
    )
    badge_text = models.CharField(max_length=50, blank=True, verbose_name="Badge Text")
    badge_class = models.CharField(
        max_length=100, 
        blank=True,
        default="hot tag",
        help_text="CSS classes for badge styling",
        verbose_name="Badge CSS Classes"
    )
    
    # Permissions and visibility
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    require_login = models.BooleanField(default=True, verbose_name="Require Login")
    required_permissions = models.TextField(
        blank=True,
        help_text="Comma-separated list of required permissions",
        verbose_name="Required Permissions"
    )
    allowed_groups = models.TextField(
        blank=True,
        help_text="Comma-separated list of allowed user groups",
        verbose_name="Allowed Groups"
    )
    
    # Ordering and metadata
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    description = models.TextField(blank=True, verbose_name="Description")
    target = models.CharField(
        max_length=20,
        choices=[
            ('_self', 'Same Window'),
            ('_blank', 'New Window'),
            ('_parent', 'Parent Frame'),
            ('_top', 'Top Frame'),
        ],
        default='_self',
        verbose_name="Link Target"
    )
    
    # Audit fields
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_menus',
        verbose_name="Created By"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category__order', 'order', 'title']
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        unique_together = ['slug', 'parent']
    
    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        return self.title
    
    def get_absolute_url(self):
        """Get the absolute URL for this menu item"""
        if self.url_name:
            try:
                if self.url_name.startswith('http'):
                    return self.url_name
                return reverse(self.url_name)
            except:
                return '#'
        return '#'
    
    def get_icon_html(self):
        """Get the HTML for the menu icon"""
        if not self.icon:
            return ''
        
        if self.icon_type == 'material':
            return f'<span class="material-symbols-outlined menu-icon">{self.icon}</span>'
        elif self.icon_type == 'feather':
            return f'<i data-feather="{self.icon}" class="menu-icon"></i>'
        else:
            return f'<i class="{self.icon} menu-icon"></i>'
    
    def has_children(self):
        """Check if this menu item has child items"""
        return self.children.filter(is_active=True).exists()
    
    def get_children(self):
        """Get active child menu items"""
        return self.children.filter(is_active=True).order_by('order', 'title')
    
    def can_user_access(self, user):
        """Check if a user can access this menu item"""
        if not self.is_active:
            return False
        
        if self.require_login and not user.is_authenticated:
            return False
        
        # Check permissions
        if self.required_permissions:
            perms = [p.strip() for p in self.required_permissions.split(',')]
            if not user.has_perms(perms):
                return False
        
        # Check groups
        if self.allowed_groups:
            groups = [g.strip() for g in self.allowed_groups.split(',')]
            user_groups = user.groups.values_list('name', flat=True)
            if not any(group in user_groups for group in groups):
                return False
        
        return True


class MenuSettings(models.Model):
    """
    Global menu settings and configuration
    """
    MENU_STYLES = [
        ('sidebar', 'Sidebar Menu'),
        ('horizontal', 'Horizontal Menu'),
        ('mixed', 'Mixed Layout'),
    ]
    
    site_name = models.CharField(max_length=200, default="Trezo", verbose_name="Site Name")
    site_logo = models.ImageField(
        upload_to='menu/logos/',
        blank=True,
        null=True,
        verbose_name="Site Logo"
    )
    logo_icon = models.CharField(
        max_length=500,
        default="/static/images/logo-icon.png",
        verbose_name="Logo Icon Path"
    )
    
    menu_style = models.CharField(max_length=20, choices=MENU_STYLES, default='sidebar')
    collapse_menu = models.BooleanField(default=False, verbose_name="Collapse Menu by Default")
    show_menu_icons = models.BooleanField(default=True, verbose_name="Show Menu Icons")
    show_menu_badges = models.BooleanField(default=True, verbose_name="Show Menu Badges")
    
    # Menu behavior
    auto_close_dropdowns = models.BooleanField(default=True, verbose_name="Auto Close Dropdowns")
    highlight_active_menu = models.BooleanField(default=True, verbose_name="Highlight Active Menu")
    
    # Customization
    custom_css = models.TextField(
        blank=True,
        help_text="Custom CSS for menu styling",
        verbose_name="Custom CSS"
    )
    custom_js = models.TextField(
        blank=True,
        help_text="Custom JavaScript for menu behavior",
        verbose_name="Custom JavaScript"
    )
    
    # Audit
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Updated By"
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Menu Settings"
        verbose_name_plural = "Menu Settings"
    
    def __str__(self):
        return f"Menu Settings - {self.site_name}"
    
    @classmethod
    def get_settings(cls):
        """Get or create menu settings"""
        settings, created = cls.objects.get_or_create(pk=1)
        return settings


class MenuLog(models.Model):
    """
    Audit log for menu changes
    """
    ACTION_TYPES = [
        ('create', 'Created'),
        ('update', 'Updated'),
        ('delete', 'Deleted'),
        ('activate', 'Activated'),
        ('deactivate', 'Deactivated'),
    ]
    
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='logs'
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='logs'
    )
    
    action = models.CharField(max_length=20, choices=ACTION_TYPES)
    description = models.TextField(verbose_name="Change Description")
    old_data = models.JSONField(null=True, blank=True, verbose_name="Old Data")
    new_data = models.JSONField(null=True, blank=True, verbose_name="New Data")
    
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="User"
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Menu Log"
        verbose_name_plural = "Menu Logs"
    
    def __str__(self):
        target = self.menu_item or self.category
        return f"{self.get_action_display()} - {target} - {self.timestamp}"
