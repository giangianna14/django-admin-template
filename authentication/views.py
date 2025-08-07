"""
Authentication views with OAuth2 support.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from allauth.socialaccount.models import SocialAccount
import logging

logger = logging.getLogger(__name__)


def login(request):
    """Login view with OAuth2 support."""
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    
    context = {
        'title': 'Login',
        'form': AuthenticationForm(),
    }
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_url = request.GET.get('next', '/dashboard/')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
        context['form'] = form
    
    return render(request, 'authentication/login.html', context)


def register(request):
    """Register view with OAuth2 support."""
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    context = {
        'title': 'Register',
        'form': UserCreationForm(),
    }
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Please correct the errors below.')
        context['form'] = form
    
    return render(request, 'authentication/register.html', context)


def forget_password(request):
    """Forget password view."""
    context = {
        'title': 'Forgot Password',
    }
    
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate password reset token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Create reset link
            reset_link = request.build_absolute_uri(
                reverse('authentication:reset-password', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Send email (in production, you'd send actual email)
            if django_settings.DEBUG:
                messages.info(request, f'Password reset link: {reset_link}')
            
            messages.success(request, 'Password reset link sent to your email!')
            return redirect('authentication:login')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that email address.')
    
    return render(request, 'authentication/forget-password.html', context)


def reset_password(request, uidb64=None, token=None):
    """Reset password view."""
    context = {
        'title': 'Reset Password',
        'validlink': False,
    }
    
    if uidb64 and token:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                context['validlink'] = True
                context['user'] = user
                
                if request.method == 'POST':
                    new_password = request.POST.get('new_password')
                    confirm_password = request.POST.get('confirm_password')
                    
                    if new_password == confirm_password:
                        user.set_password(new_password)
                        user.save()
                        messages.success(request, 'Password reset successful! You can now log in.')
                        return redirect('authentication:login')
                    else:
                        messages.error(request, 'Passwords do not match.')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            messages.error(request, 'Invalid reset link.')
    
    return render(request, 'authentication/reset-password.html', context)


@login_required
def logout(request):
    """Logout view."""
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('core:home')


def lock_screen(request):
    """Lock screen view."""
    if not request.user.is_authenticated:
        return redirect('authentication:login')
    
    context = {
        'title': 'Lock Screen',
        'user': request.user,
    }
    
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            messages.success(request, 'Screen unlocked successfully!')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Invalid password.')
    
    return render(request, 'authentication/lock-screen.html', context)


def confirm_mail(request):
    """Email confirmation view."""
    context = {
        'title': 'Confirm Email',
    }
    return render(request, 'authentication/confirm-mail.html', context)


@login_required
def profile(request):
    """User profile view."""
    social_accounts = SocialAccount.objects.filter(user=request.user)
    
    context = {
        'title': 'Profile',
        'user': request.user,
        'social_accounts': social_accounts,
    }
    
    if request.method == 'POST':
        # Update user profile
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('authentication:profile')
    
    return render(request, 'authentication/profile.html', context)


@login_required
def settings(request):
    """User settings view."""
    context = {
        'title': 'Settings',
        'user': request.user,
    }
    return render(request, 'authentication/settings.html', context)


@login_required
def account_settings(request):
    """Account settings view."""
    context = {
        'title': 'Account Settings',
        'user': request.user,
    }
    return render(request, 'authentication/account-settings.html', context)


@login_required
def change_password(request):
    """Change password view."""
    context = {
        'title': 'Change Password',
    }
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        elif len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        else:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('authentication:login')
    
    return render(request, 'authentication/change-password.html', context)


@login_required
def connections(request):
    """Social connections view."""
    social_accounts = SocialAccount.objects.filter(user=request.user)
    
    context = {
        'title': 'Social Connections',
        'user': request.user,
        'social_accounts': social_accounts,
        'connected_providers': [acc.provider for acc in social_accounts],
    }
    return render(request, 'authentication/connections.html', context)


def password_reset(request):
    """Password reset request view."""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            
            # Generate token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Create reset URL
            reset_url = request.build_absolute_uri(
                reverse('authentication:password_reset_confirm', 
                       kwargs={'uidb64': uid, 'token': token})
            )
            
            # Send email
            subject = 'Password Reset Request'
            message = render_to_string('authentication/password_reset_email.html', {
                'user': user,
                'reset_url': reset_url,
                'site_name': 'Django Admin Template',
            })
            
            send_mail(
                subject,
                message,
                django_settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            return redirect('authentication:password_reset_done')
            
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email address.')
    
    return render(request, 'authentication/password_reset.html')


def password_reset_done(request):
    """Password reset done view."""
    return render(request, 'authentication/password_reset_done.html')


def password_reset_confirm(request, uidb64, token):
    """Password reset confirm view."""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password has been reset successfully.')
                return redirect('authentication:password_reset_complete')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = SetPasswordForm(user)
        
        context = {
            'form': form,
            'validlink': True,
        }
        return render(request, 'authentication/password_reset_confirm.html', context)
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('authentication:password_reset')


def password_reset_complete(request):
    """Password reset complete view."""
    return render(request, 'authentication/password_reset_complete.html')
