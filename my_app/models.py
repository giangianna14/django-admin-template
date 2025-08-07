from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os
from PIL import Image

def user_profile_picture_path(instance, filename):
    """Generate path for user profile pictures"""
    return f'profile_pictures/{instance.user.username}/{filename}'

def user_cover_photo_path(instance, filename):
    """Generate path for user cover photos"""
    return f'cover_photos/{instance.user.username}/{filename}'

class UserProfile(models.Model):
    PRIVACY_CHOICES = [
        ('only_me', 'Only Me'),
        ('followers', 'My Followers'),
        ('everyone', 'Everyone'),
    ]
    
    TAG_CHOICES = [
        ('everyone', 'Everyone'),
        ('group_member', 'Group Member'),
    ]
    
    SKILL_CHOICES = [
        ('leadership', 'Leadership'),
        ('data_analysis', 'Data Analysis'),
        ('project_management', 'Project Management'),
        ('teamwork', 'Teamwork'),
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('sales', 'Sales'),
    ]
    
    PROFESSION_CHOICES = [
        ('financial_manager', 'Financial Manager'),
        ('it_manager', 'IT Manager'),
        ('software_developer', 'Software Developer'),
        ('physician_assistant', 'Physician Assistant'),
        ('marketing_manager', 'Marketing Manager'),
        ('sales_manager', 'Sales Manager'),
        ('designer', 'Designer'),
        ('consultant', 'Consultant'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Personal Information
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True, help_text="Tell us about yourself")
    
    # Professional Information
    skills = models.CharField(max_length=50, choices=SKILL_CHOICES, blank=True, null=True)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    
    # Images
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, blank=True, null=True)
    cover_photo = models.ImageField(upload_to=user_cover_photo_path, blank=True, null=True)
    
    # Privacy Settings
    profile_visibility = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default='everyone')
    show_email = models.BooleanField(default=False)
    show_experiences = models.BooleanField(default=True)
    show_followers = models.BooleanField(default=True)
    who_can_tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='everyone')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize profile picture if it exists
        if self.profile_picture:
            self.resize_image(self.profile_picture.path, (300, 300))
        
        # Resize cover photo if it exists
        if self.cover_photo:
            self.resize_image(self.cover_photo.path, (1200, 400))
    
    def resize_image(self, image_path, size):
        """Resize image to specified size"""
        try:
            with Image.open(image_path) as img:
                img.thumbnail(size, Image.Resampling.LANCZOS)
                img.save(image_path, optimize=True, quality=85)
        except Exception as e:
            print(f"Error resizing image: {e}")
    
    def get_profile_picture_url(self):
        """Get profile picture URL or default"""
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/images/user-default.png'
    
    def get_cover_photo_url(self):
        """Get cover photo URL or default"""
        if self.cover_photo:
            return self.cover_photo.url
        return '/static/images/cover-default.jpg'
    
    @property
    def full_name(self):
        """Get user's full name"""
        return self.user.get_full_name() or self.user.username
    
    @property
    def display_skills(self):
        """Get human readable skills"""
        if self.skills:
            return dict(self.SKILL_CHOICES).get(self.skills, self.skills)
        return None
    
    @property
    def display_profession(self):
        """Get human readable profession"""
        if self.profession:
            return dict(self.PROFESSION_CHOICES).get(self.profession, self.profession)
        return None
