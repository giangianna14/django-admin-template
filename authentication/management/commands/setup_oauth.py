"""
Management command to setup OAuth2 providers easily.
"""
from django.core.management.base import BaseCommand, CommandError
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.db import transaction


class Command(BaseCommand):
    help = 'Setup OAuth2 social applications for Google, Facebook, and Apple'

    def add_arguments(self, parser):
        parser.add_argument(
            '--provider',
            type=str,
            choices=['google', 'facebook', 'apple', 'all'],
            default='all',
            help='Which provider to setup (default: all)'
        )
        parser.add_argument(
            '--google-client-id',
            type=str,
            help='Google OAuth2 Client ID'
        )
        parser.add_argument(
            '--google-secret',
            type=str,
            help='Google OAuth2 Client Secret'
        )
        parser.add_argument(
            '--facebook-app-id',
            type=str,
            help='Facebook App ID'
        )
        parser.add_argument(
            '--facebook-secret',
            type=str,
            help='Facebook App Secret'
        )
        parser.add_argument(
            '--apple-service-id',
            type=str,
            help='Apple Service ID'
        )
        parser.add_argument(
            '--apple-secret',
            type=str,
            help='Apple Client Secret (JWT)'
        )
        parser.add_argument(
            '--apple-team-id',
            type=str,
            help='Apple Team ID'
        )
        parser.add_argument(
            '--demo',
            action='store_true',
            help='Setup with demo/placeholder credentials for testing'
        )

    def handle(self, *args, **options):
        try:
            site = Site.objects.get_current()
            self.stdout.write(f"Setting up OAuth2 providers for site: {site.domain}")
            
            with transaction.atomic():
                if options['provider'] in ['google', 'all']:
                    self.setup_google(options, site)
                
                if options['provider'] in ['facebook', 'all']:
                    self.setup_facebook(options, site)
                
                if options['provider'] in ['apple', 'all']:
                    self.setup_apple(options, site)
            
            self.stdout.write(
                self.style.SUCCESS('✅ OAuth2 providers setup completed successfully!')
            )
            self.stdout.write(
                self.style.WARNING('⚠️  Remember to update credentials with real values in production!')
            )
            
        except Exception as e:
            raise CommandError(f'Error setting up OAuth2 providers: {str(e)}')

    def setup_google(self, options, site):
        """Setup Google OAuth2 provider."""
        if options['demo']:
            client_id = 'demo-google-client-id-replace-with-real'
            secret = 'demo-google-secret-replace-with-real'
        else:
            client_id = options.get('google_client_id')
            secret = options.get('google_secret')
            
            if not client_id or not secret:
                self.stdout.write(
                    self.style.WARNING('⚠️  Google credentials not provided, using demo values')
                )
                client_id = 'demo-google-client-id-replace-with-real'
                secret = 'demo-google-secret-replace-with-real'

        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google OAuth2',
                'client_id': client_id,
                'secret': secret,
            }
        )
        
        if not created:
            google_app.client_id = client_id
            google_app.secret = secret
            google_app.save()
            
        google_app.sites.add(site)
        
        action = "Created" if created else "Updated"
        self.stdout.write(f"🔵 {action} Google OAuth2 application")

    def setup_facebook(self, options, site):
        """Setup Facebook OAuth2 provider."""
        if options['demo']:
            client_id = 'demo-facebook-app-id-replace-with-real'
            secret = 'demo-facebook-secret-replace-with-real'
        else:
            client_id = options.get('facebook_app_id')
            secret = options.get('facebook_secret')
            
            if not client_id or not secret:
                self.stdout.write(
                    self.style.WARNING('⚠️  Facebook credentials not provided, using demo values')
                )
                client_id = 'demo-facebook-app-id-replace-with-real'
                secret = 'demo-facebook-secret-replace-with-real'

        facebook_app, created = SocialApp.objects.get_or_create(
            provider='facebook',
            defaults={
                'name': 'Facebook OAuth2',
                'client_id': client_id,
                'secret': secret,
            }
        )
        
        if not created:
            facebook_app.client_id = client_id
            facebook_app.secret = secret
            facebook_app.save()
            
        facebook_app.sites.add(site)
        
        action = "Created" if created else "Updated"
        self.stdout.write(f"🔵 {action} Facebook OAuth2 application")

    def setup_apple(self, options, site):
        """Setup Apple OAuth2 provider."""
        if options['demo']:
            client_id = 'demo-apple-service-id-replace-with-real'
            secret = 'demo-apple-jwt-secret-replace-with-real'
            key = 'demo-apple-team-id-replace-with-real'
        else:
            client_id = options.get('apple_service_id')
            secret = options.get('apple_secret')
            key = options.get('apple_team_id')
            
            if not client_id or not secret or not key:
                self.stdout.write(
                    self.style.WARNING('⚠️  Apple credentials not provided, using demo values')
                )
                client_id = 'demo-apple-service-id-replace-with-real'
                secret = 'demo-apple-jwt-secret-replace-with-real'
                key = 'demo-apple-team-id-replace-with-real'

        apple_app, created = SocialApp.objects.get_or_create(
            provider='apple',
            defaults={
                'name': 'Apple OAuth2',
                'client_id': client_id,
                'secret': secret,
                'key': key,
            }
        )
        
        if not created:
            apple_app.client_id = client_id
            apple_app.secret = secret
            apple_app.key = key
            apple_app.save()
            
        apple_app.sites.add(site)
        
        action = "Created" if created else "Updated"
        self.stdout.write(f"⚫ {action} Apple OAuth2 application")
