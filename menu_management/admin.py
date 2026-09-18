"""
Menu Management Admin Interface

Provides Django admin interface for managing menus, categories, and settings.
"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
from .models import MenuCategory, MenuItem, MenuSettings, MenuLog


class MenuItemInline(admin.TabularInline):
    """Inline admin for child menu items"""
    model = MenuItem
    extra = 0
    fields = ('title', 'slug', 'url_name', 'icon', 'order', 'is_active')
    show_change_link = True


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    """Admin interface for menu categories"""
    list_display = ('name', 'category_type', 'order', 'menu_count', 'is_active', 'created_at')
    list_filter = ('category_type', 'is_active', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')
    inlines = [MenuItemInline]
    
    def menu_count(self, obj):
        """Count of menu items in this category"""
        count = obj.menu_items.count()
        if count:
            url = reverse('admin:menu_management_menuitem_changelist')
            return format_html(
                '<a href="{}?category__id__exact={}">{} items</a>',
                url, obj.id, count
            )
        return '0 items'
    menu_count.short_description = 'Menu Items'


class MenuItemAdminForm(forms.ModelForm):
    """Custom form for menu item admin"""
    
    class Meta:
        model = MenuItem
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'required_permissions': forms.Textarea(attrs={'rows': 2}),
            'allowed_groups': forms.Textarea(attrs={'rows': 2}),
        }


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin interface for menu items"""
    form = MenuItemAdminForm
    list_display = (
        'display_title', 'category', 'menu_type', 'url_display', 
        'order', 'badge_display', 'is_active', 'created_at'
    )
    list_filter = (
        'category', 'menu_type', 'is_active', 'require_login', 
        'icon_type', 'created_at', 'parent'
    )
    search_fields = ('title', 'slug', 'url_name', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('category__order', 'order', 'title')
    raw_id_fields = ('parent', 'created_by')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category', 'parent')
        }),
        ('URL & Navigation', {
            'fields': ('url_name', 'url_pattern', 'target', 'menu_type')
        }),
        ('Display Properties', {
            'fields': (
                'icon_type', 'icon', 'badge_text', 'badge_class', 'order'
            ),
            'classes': ('collapse',)
        }),
        ('Permissions & Access', {
            'fields': (
                'is_active', 'require_login', 'required_permissions', 'allowed_groups'
            ),
            'classes': ('collapse',)
        }),
        ('Audit Information', {
            'fields': ('created_by',),
            'classes': ('collapse',)
        })
    )
    
    def display_title(self, obj):
        """Display title with hierarchy indication"""
        if obj.parent:
            return format_html(
                '<span style="margin-left: 20px;">└─ {}</span>',
                obj.title
            )
        return obj.title
    display_title.short_description = 'Title'
    display_title.admin_order_field = 'title'
    
    def url_display(self, obj):
        """Display URL with link if valid"""
        if obj.url_name:
            try:
                url = obj.get_absolute_url()
                if url != '#':
                    return format_html('<a href="{}" target="_blank">{}</a>', url, obj.url_name)
            except:
                pass
            return obj.url_name
        return '-'
    url_display.short_description = 'URL'
    
    def badge_display(self, obj):
        """Display badge if exists"""
        if obj.badge_text:
            return format_html(
                '<span class="{}">{}</span>',
                obj.badge_class or 'badge badge-primary',
                obj.badge_text
            )
        return '-'
    badge_display.short_description = 'Badge'
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        qs = super().get_queryset(request)
        return qs.select_related('category', 'parent', 'created_by')
    
    def save_model(self, request, obj, form, change):
        """Save model with audit information"""
        if not change:  # Creating new
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(MenuSettings)
class MenuSettingsAdmin(admin.ModelAdmin):
    """Admin interface for menu settings"""
    fieldsets = (
        ('Site Branding', {
            'fields': ('site_name', 'site_logo', 'logo_icon')
        }),
        ('Menu Layout', {
            'fields': (
                'menu_style', 'collapse_menu', 'show_menu_icons', 
                'show_menu_badges'
            )
        }),
        ('Menu Behavior', {
            'fields': ('auto_close_dropdowns', 'highlight_active_menu')
        }),
        ('Customization', {
            'fields': ('custom_css', 'custom_js'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Only allow one settings instance"""
        return not MenuSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Don't allow deletion of settings"""
        return False
    
    def save_model(self, request, obj, form, change):
        """Save with audit information"""
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(MenuLog)
class MenuLogAdmin(admin.ModelAdmin):
    """Admin interface for menu logs (read-only)"""
    list_display = (
        'timestamp', 'action', 'target_display', 'user', 'ip_address'
    )
    list_filter = ('action', 'timestamp')
    search_fields = ('description', 'user__username')
    ordering = ('-timestamp',)
    readonly_fields = (
        'menu_item', 'category', 'action', 'description', 
        'old_data', 'new_data', 'user', 'ip_address', 'timestamp'
    )
    
    def target_display(self, obj):
        """Display the target of the log entry"""
        if obj.menu_item:
            return f"Menu: {obj.menu_item.title}"
        elif obj.category:
            return f"Category: {obj.category.name}"
        return "Unknown"
    target_display.short_description = 'Target'
    
    def has_add_permission(self, request):
        """Don't allow manual log creation"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Don't allow log editing"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Don't allow log deletion"""
        return False


# Register admin actions
def activate_menus(modeladmin, request, queryset):
    """Bulk activate menu items"""
    queryset.update(is_active=True)
    modeladmin.message_user(request, f"Activated {queryset.count()} menu items.")

def deactivate_menus(modeladmin, request, queryset):
    """Bulk deactivate menu items"""
    queryset.update(is_active=False)
    modeladmin.message_user(request, f"Deactivated {queryset.count()} menu items.")

activate_menus.short_description = "Activate selected menu items"
deactivate_menus.short_description = "Deactivate selected menu items"

MenuItemAdmin.actions = [activate_menus, deactivate_menus]
