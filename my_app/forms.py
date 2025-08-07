from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True)

class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information"""
    
    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'address', 'country', 'bio', 'skills', 'profession',
            'company_name', 'company_website', 'facebook_url', 'twitter_url',
            'linkedin_url', 'youtube_url', 'instagram_url', 'github_url',
            'profile_picture', 'cover_photo', 'profile_visibility', 'show_email',
            'show_experiences', 'show_followers', 'who_can_tag'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': '+1 444 555 6699'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'E.g. 84 S. Arrowhead Court Branford'
            }),
            'country': forms.Select(attrs={
                'class': 'form-select form-control h-55'
            }, choices=[
                ('', 'Select Country'),
                ('ID', 'Indonesia'),
                ('US', 'United States'),
                ('UK', 'United Kingdom'),
                ('CA', 'Canada'),
                ('AU', 'Australia'),
                ('DE', 'Germany'),
                ('FR', 'France'),
                ('JP', 'Japan'),
                ('SG', 'Singapore'),
                ('MY', 'Malaysia'),
            ]),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Tell us about yourself...'
            }),
            'skills': forms.Select(attrs={'class': 'form-select form-control h-55'}),
            'profession': forms.Select(attrs={'class': 'form-select form-control h-55'}),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'Your Company Name'
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://yourcompany.com'
            }),
            'facebook_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://www.facebook.com/yourprofile'
            }),
            'twitter_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://twitter.com/yourhandle'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://www.linkedin.com/in/yourprofile'
            }),
            'youtube_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://www.youtube.com/c/yourchannel'
            }),
            'instagram_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://www.instagram.com/yourhandle'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'https://github.com/yourusername'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'cover_photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'profile_visibility': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'who_can_tag': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'show_email': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_experiences': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_followers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserAccountForm(forms.ModelForm):
    """Form for updating basic user account information"""
    
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control h-55',
            'placeholder': 'Enter current password'
        }),
        required=False,
        help_text="Required only if changing password"
    )
    
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control h-55',
            'placeholder': 'Enter new password'
        }),
        required=False,
        help_text="Leave blank if you don't want to change password"
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control h-55',
            'placeholder': 'Confirm new password'
        }),
        required=False
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'your.email@example.com'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control h-55',
                'placeholder': 'Username'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password:
            if not current_password:
                raise forms.ValidationError("Current password is required to set a new password.")
            
            if new_password != confirm_password:
                raise forms.ValidationError("New passwords do not match.")
            
            # Validate current password
            user = getattr(self, 'instance', None)
            if user and not user.check_password(current_password):
                raise forms.ValidationError("Current password is incorrect.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password')
        
        if new_password:
            user.set_password(new_password)
        
        if commit:
            user.save()
        return user
