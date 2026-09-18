"""
Menu Management Forms

Provides forms for managing menus, categories, and settings.
"""
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from .models import MenuCategory, MenuItem, MenuSettings


class MenuCategoryForm(forms.ModelForm):
    """Form for creating and editing menu categories"""
    
    class Meta:
        model = MenuCategory
        fields = ['name', 'slug', 'category_type', 'order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'auto-generated-slug'
            }),
            'category_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].help_text = 'Leave blank to auto-generate from name'
        
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            # Auto-generate slug from name
            name = self.cleaned_data.get('name', '')
            slug = name.lower().replace(' ', '-').replace('_', '-')
            # Remove special characters
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        return slug


class MenuItemForm(forms.ModelForm):
    """Form for creating and editing menu items"""
    
    class Meta:
        model = MenuItem
        fields = [
            'title', 'slug', 'category', 'parent', 'menu_type',
            'url_name', 'url_pattern', 'target',
            'icon_type', 'icon', 'badge_text', 'badge_class',
            'order', 'description', 'is_active', 'require_login',
            'required_permissions', 'allowed_groups'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter menu title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'auto-generated-slug'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'parent': forms.Select(attrs={
                'class': 'form-select'
            }),
            'menu_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'url_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., dashboard:index or /custom-url/'
            }),
            'url_pattern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., /dashboard/'
            }),
            'target': forms.Select(attrs={
                'class': 'form-select'
            }),
            'icon_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., dashboard, shopping_cart'
            }),
            'badge_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., New, Hot'
            }),
            'badge_class': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., hot tag, badge-primary'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'required_permissions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'e.g., auth.view_user, myapp.change_model'
            }),
            'allowed_groups': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'e.g., Administrators, Managers'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'require_login': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter parent choices to exclude current item and its descendants
        if self.instance.pk:
            # Get all descendants to exclude
            descendants = self.get_descendants(self.instance)
            exclude_ids = [self.instance.pk] + [d.pk for d in descendants]
            self.fields['parent'].queryset = MenuItem.objects.exclude(
                pk__in=exclude_ids
            ).order_by('category__order', 'order', 'title')
        else:
            self.fields['parent'].queryset = MenuItem.objects.order_by(
                'category__order', 'order', 'title'
            )
        
        # Add empty choice for parent
        self.fields['parent'].empty_label = "No Parent (Top Level)"
        
        # Help texts
        self.fields['slug'].help_text = 'Leave blank to auto-generate from title'
        self.fields['url_name'].help_text = 'Django URL name or absolute URL'
        self.fields['url_pattern'].help_text = 'Pattern for checking active state'
        self.fields['required_permissions'].help_text = 'Comma-separated permissions'
        self.fields['allowed_groups'].help_text = 'Comma-separated group names'
    
    def get_descendants(self, item):
        """Get all descendants of a menu item"""
        descendants = []
        children = item.children.all()
        for child in children:
            descendants.append(child)
            descendants.extend(self.get_descendants(child))
        return descendants
    
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            # Auto-generate slug from title
            title = self.cleaned_data.get('title', '')
            slug = title.lower().replace(' ', '-').replace('_', '-')
            # Remove special characters
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        return slug
    
    def clean_parent(self):
        parent = self.cleaned_data.get('parent')
        category = self.cleaned_data.get('category')
        
        # Validate parent is in same category
        if parent and category and parent.category != category:
            raise ValidationError(
                'Parent menu item must be in the same category.'
            )
        
        return parent
    
    def clean(self):
        cleaned_data = super().clean()
        menu_type = cleaned_data.get('menu_type')
        url_name = cleaned_data.get('url_name')
        parent = cleaned_data.get('parent')
        
        # Validate URL for link type menus
        if menu_type == 'link' and not url_name:
            self.add_error('url_name', 'URL is required for link type menus.')
        
        # Validate parent for dropdown menus
        if menu_type == 'dropdown' and parent:
            self.add_error('parent', 'Dropdown menus cannot have a parent.')
        
        return cleaned_data


class MenuSettingsForm(forms.ModelForm):
    """Form for menu settings"""
    
    class Meta:
        model = MenuSettings
        fields = [
            'site_name', 'site_logo', 'logo_icon', 'menu_style',
            'collapse_menu', 'show_menu_icons', 'show_menu_badges',
            'auto_close_dropdowns', 'highlight_active_menu',
            'custom_css', 'custom_js'
        ]
        widgets = {
            'site_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'logo_icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/static/images/logo-icon.png'
            }),
            'menu_style': forms.Select(attrs={
                'class': 'form-select'
            }),
            'collapse_menu': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'show_menu_icons': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'show_menu_badges': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'auto_close_dropdowns': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'highlight_active_menu': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'custom_css': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': '/* Custom CSS for menu styling */'
            }),
            'custom_js': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': '// Custom JavaScript for menu behavior'
            })
        }


class MenuReorderForm(forms.Form):
    """Form for reordering menu items"""
    category = forms.ModelChoiceField(
        queryset=MenuCategory.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Select category to reorder its menu items"
    )


class MenuSearchForm(forms.Form):
    """Form for searching menus"""
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search menus...'
        })
    )
    category = forms.ModelChoiceField(
        queryset=MenuCategory.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ChoiceField(
        choices=[
            ('', 'All Status'),
            ('active', 'Active'),
            ('inactive', 'Inactive')
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class MenuImportForm(forms.Form):
    """Form for importing menu structure"""
    import_file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.json,.csv'
        }),
        help_text="Upload JSON or CSV file with menu structure"
    )
    replace_existing = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        help_text="Replace existing menus with imported data"
    )


class MenuExportForm(forms.Form):
    """Form for exporting menu structure"""
    EXPORT_FORMATS = [
        ('json', 'JSON'),
        ('csv', 'CSV'),
        ('xml', 'XML')
    ]
    
    categories = forms.ModelMultipleChoiceField(
        queryset=MenuCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        help_text="Select categories to export"
    )
    format = forms.ChoiceField(
        choices=EXPORT_FORMATS,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial='json'
    )
    include_inactive = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        help_text="Include inactive menu items"
    )
