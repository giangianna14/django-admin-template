from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from decouple import config


class Command(BaseCommand):
    help = 'Setup Google OAuth2 configuration'

    def handle(self, *args, **options):
        # Get or create the current site
        site, created = Site.objects.get_or_create(
            pk=1,
            defaults={
                'domain': '127.0.0.1:8000',
                'name': 'Django Bootstrap Local'
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created site: {site.domain}')
            )
        else:
            # Update site domain if needed
            site.domain = '127.0.0.1:8000'
            site.name = 'Django Bootstrap Local'
            site.save()
            self.stdout.write(
                self.style.SUCCESS(f'Updated site: {site.domain}')
            )

        # Get Google OAuth credentials from environment
        google_client_id = config('GOOGLE_OAUTH2_KEY', default='')
        google_secret = config('GOOGLE_OAUTH2_SECRET', default='')

        if not google_client_id or not google_secret or google_client_id == '' or google_secret == '':
            self.stdout.write(
                self.style.ERROR('Google OAuth credentials not found in .env file!')
            )
            self.stdout.write('Please set GOOGLE_OAUTH2_KEY and GOOGLE_OAUTH2_SECRET in your .env file')
            return

        # Create or update Google OAuth app
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google OAuth2',
                'client_id': str(google_client_id),
                'secret': str(google_secret),
            }
        )

        if not created:
            # Update existing app
            google_app.client_id = str(google_client_id)
            google_app.secret = str(google_secret)
            google_app.save()
            self.stdout.write(
                self.style.SUCCESS('Updated Google OAuth2 app')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Created Google OAuth2 app')
            )

        # Add site to the app
        google_app.sites.add(site)
        
        self.stdout.write(
            self.style.SUCCESS('Google OAuth2 setup completed!')
        )
        self.stdout.write(f'Site: {site.domain}')
        self.stdout.write(f'Google Client ID: {str(google_client_id)[:20]}...')
        self.stdout.write('')
        self.stdout.write('Make sure to configure the following in Google Console:')
        self.stdout.write('- Authorized JavaScript origins: http://127.0.0.1:8000')
        self.stdout.write('- Authorized redirect URIs: http://127.0.0.1:8000/accounts/google/login/callback/')
