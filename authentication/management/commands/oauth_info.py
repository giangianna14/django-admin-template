"""
Management command to display OAuth2 setup information.
"""
from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.conf import settings


class Command(BaseCommand):
    help = 'Display OAuth2 setup information and guide'

    def handle(self, *args, **options):
        self.stdout.write("=== OAuth2 Setup Information ===\n")
        
        # Current site info
        site = Site.objects.get_current()
        self.stdout.write(f"🌐 Current site: {site.domain}")
        self.stdout.write(f"📝 Site name: {site.name}\n")
        
        # Check installed apps
        required_apps = [
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'allauth.socialaccount.providers.google',
            'allauth.socialaccount.providers.facebook', 
            'allauth.socialaccount.providers.apple',
        ]
        
        self.stdout.write("📦 Required apps status:")
        for app in required_apps:
            status = "✅" if app in settings.INSTALLED_APPS else "❌"
            self.stdout.write(f"  {status} {app}")
        self.stdout.write("")
        
        # Social apps in database
        social_apps = SocialApp.objects.all()
        self.stdout.write(f"🔐 Social Applications ({social_apps.count()} total):")
        
        if not social_apps:
            self.stdout.write("  ❌ No social applications found!")
            self.stdout.write("  💡 Run: python manage.py setup_oauth --demo")
        else:
            for app in social_apps:
                icon = {
                    'google': '🔵',
                    'facebook': '🔵', 
                    'apple': '⚫',
                }.get(app.provider, '🔹')
                
                sites_count = app.sites.count()
                is_demo = 'demo-' in app.client_id
                demo_text = " (DEMO)" if is_demo else ""
                
                self.stdout.write(f"  {icon} {app.name} ({app.provider}){demo_text}")
                self.stdout.write(f"    Client ID: {app.client_id[:20]}...")
                self.stdout.write(f"    Sites: {sites_count} assigned")
        
        self.stdout.write("\n=== Setup URLs ===")
        self.stdout.write("🌐 Django Admin: http://localhost:8000/admin/")
        self.stdout.write("🔐 Social Apps: http://localhost:8000/admin/socialaccount/socialapp/")
        self.stdout.write("🔑 Login Page: http://localhost:8000/auth/login/")
        
        self.stdout.write("\n=== Quick Actions ===")
        self.stdout.write("📝 Setup demo OAuth2: python manage.py setup_oauth --demo")
        self.stdout.write("🔑 Create superuser: python manage.py createsuperuser")
        self.stdout.write("🚀 Run server: python manage.py runserver")
        
        self.stdout.write("\n=== OAuth2 Provider Setup ===")
        
        providers = [
            {
                'name': 'Google',
                'icon': '🔵',
                'console': 'https://console.cloud.google.com/',
                'redirect': 'http://localhost:8000/accounts/google/login/callback/',
                'steps': [
                    'Create project in Google Cloud Console',
                    'Enable Google+ API or Google Identity API',
                    'Create OAuth 2.0 credentials',
                    'Add authorized redirect URIs',
                    'Copy Client ID and Secret to Django admin'
                ]
            },
            {
                'name': 'Facebook',
                'icon': '🔵',
                'console': 'https://developers.facebook.com/',
                'redirect': 'http://localhost:8000/accounts/facebook/login/callback/',
                'steps': [
                    'Create app in Facebook Developers',
                    'Add Facebook Login product',
                    'Configure Valid OAuth Redirect URIs',
                    'Copy App ID and App Secret to Django admin'
                ]
            },
            {
                'name': 'Apple',
                'icon': '⚫',
                'console': 'https://developer.apple.com/',
                'redirect': 'http://localhost:8000/accounts/apple/login/callback/',
                'steps': [
                    'Create App ID in Apple Developer',
                    'Create Service ID for Sign in with Apple',
                    'Configure return URLs',
                    'Generate and download private key',
                    'Create JWT token and add to Django admin'
                ]
            }
        ]
        
        for provider in providers:
            self.stdout.write(f"\n{provider['icon']} {provider['name']} Setup:")
            self.stdout.write(f"  Console: {provider['console']}")
            self.stdout.write(f"  Redirect URI: {provider['redirect']}")
            for i, step in enumerate(provider['steps'], 1):
                self.stdout.write(f"  {i}. {step}")
        
        self.stdout.write(f"\n✅ Setup complete! Visit Django admin to configure real credentials.")
        
        # Check if demo credentials are being used
        demo_apps = social_apps.filter(client_id__startswith='demo-')
        if demo_apps.exists():
            self.stdout.write(
                self.style.WARNING(
                    f"\n⚠️  Warning: {demo_apps.count()} app(s) using demo credentials. "
                    "Update with real credentials for production!"
                )
            )
