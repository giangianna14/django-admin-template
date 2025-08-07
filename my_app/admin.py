from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Unregister the default User admin
admin.site.unregister(User)

# Define an inline admin descriptor for UserProfile model
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'
    
    # Fields to display in admin
    fields = (
        'bio', 'profession', 'skills', 'phone_number', 'address', 'country',
        'company_name', 'company_website',
        'profile_picture', 'cover_photo',
        'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'github_url',
        'profile_visibility', 'show_email', 'show_experiences', 'show_followers', 'who_can_tag'
    )

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    
    # Add profile fields to the user list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)

# Register the new UserAdmin
admin.site.register(User, UserAdmin)

# Register UserProfile separately for direct management
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'phone_number', 'country', 'created_at', 'updated_at')
    list_filter = ('profession', 'skills', 'profile_visibility', 'show_email', 'show_experiences', 'show_followers')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email', 'phone_number', 'company_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'bio', 'profession', 'skills')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'address', 'country', 'company_name', 'company_website')
        }),
        ('Media', {
            'fields': ('profile_picture', 'cover_photo')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'github_url')
        }),
        ('Privacy Settings', {
            'fields': ('profile_visibility', 'show_email', 'show_experiences', 'show_followers', 'who_can_tag')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

# Customize admin site header and title
admin.site.site_header = 'Django Bootstrap Admin'
admin.site.site_title = 'Django Bootstrap Admin Portal'
admin.site.index_title = 'Welcome to Django Bootstrap Administration'
