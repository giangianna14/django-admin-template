#!/usr/bin/env python3

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_google_oauth_demo():
    """
    Setup Google OAuth2 configuration dengan dummy credentials untuk demo
    """
    
    # Update site domain
    site = Site.objects.get(id=1)
    site.domain = '127.0.0.1:8000'
    site.name = 'Django Bootstrap App'
    site.save()
    
    print("✅ Site domain updated successfully!")
    print(f"Site: {site.domain}")
    
    # Create Google OAuth app dengan dummy credentials
    client_id = "your-google-client-id.googleusercontent.com"
    client_secret = "your-google-client-secret"
    
    # Check if Google app already exists
    google_app, created = SocialApp.objects.get_or_create(
        provider='google',
        defaults={
            'name': 'Google OAuth2',
            'client_id': client_id,
            'secret': client_secret,
        }
    )
    
    if not created:
        google_app.client_id = client_id
        google_app.secret = client_secret
        google_app.save()
    
    # Add site to the app
    google_app.sites.add(site)
    
    if created:
        print("✅ Google OAuth app created successfully!")
    else:
        print("✅ Google OAuth app updated successfully!")
    
    print(f"Provider: {google_app.provider}")
    print(f"Client ID: {google_app.client_id}")
    print(f"Sites: {[s.domain for s in google_app.sites.all()]}")
    
    print("\n🔧 Setup Instructions untuk Credentials Asli:")
    print("1. Go to https://console.developers.google.com/")
    print("2. Create a new project or select existing one")
    print("3. Enable Google+ API")
    print("4. Create OAuth 2.0 credentials")
    print("5. Add this redirect URI: http://127.0.0.1:8000/accounts/google/login/callback/")
    print("6. Update credentials di Django Admin: http://127.0.0.1:8000/admin/socialaccount/socialapp/")
    print("\n🚀 Google OAuth2 demo setup selesai!")

if __name__ == '__main__':
    setup_google_oauth_demo()
