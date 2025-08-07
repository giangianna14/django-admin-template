# Setup OAuth2 Providers di Django Admin

## Langkah-langkah Setup OAuth2:

### 1. Akses Django Admin
1. Pastikan server berjalan: `python manage.py runserver`
2. Buka: http://localhost:8000/admin/
3. Login dengan superuser account

### 2. Setup Google OAuth2

#### A. Buat Google Cloud Project
1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru atau pilih existing
3. Enable "Google+ API" atau "Google Identity API"
4. Pergi ke **Credentials** → **Create Credentials** → **OAuth 2.0 Client IDs**

#### B. Konfigurasi OAuth2 Client
- **Application type**: Web application
- **Name**: Django Admin Template
- **Authorized JavaScript origins**:
  ```
  http://localhost:8000
  https://yourdomain.com
  ```
- **Authorized redirect URIs**:
  ```
  http://localhost:8000/accounts/google/login/callback/
  https://yourdomain.com/accounts/google/login/callback/
  ```

#### C. Tambah di Django Admin
1. Pergi ke **Social Applications** → **Add Social Application**
2. **Provider**: Google
3. **Name**: Google OAuth2
4. **Client id**: (copy dari Google Console)
5. **Secret key**: (copy dari Google Console)
6. **Sites**: Pilih "example.com" (default site)
7. **Save**

### 3. Setup Facebook OAuth2

#### A. Buat Facebook App
1. Buka [Facebook Developers](https://developers.facebook.com/)
2. **Create App** → **Consumer** → **Next**
3. **App name**: Django Admin Template
4. Tambah **Facebook Login** product

#### B. Konfigurasi Facebook Login
- **Valid OAuth Redirect URIs**:
  ```
  http://localhost:8000/accounts/facebook/login/callback/
  https://yourdomain.com/accounts/facebook/login/callback/
  ```
- **Client token**: Generate di Settings → Advanced

#### C. Tambah di Django Admin
1. **Social Applications** → **Add Social Application**
2. **Provider**: Facebook
3. **Name**: Facebook OAuth2
4. **Client id**: App ID dari Facebook
5. **Secret key**: App Secret dari Facebook
6. **Sites**: Pilih "example.com"
7. **Save**

### 4. Setup Apple OAuth2

#### A. Apple Developer Setup
1. Buka [Apple Developer](https://developer.apple.com/account/)
2. **Certificates, Identifiers & Profiles**
3. **Identifiers** → **App IDs** → Buat baru
4. **Services** → **Sign In with Apple** → Configure

#### B. Buat Service ID
1. **Identifiers** → **Services IDs** → Buat baru
2. **Configure Sign In with Apple**
3. **Return URLs**:
   ```
   http://localhost:8000/accounts/apple/login/callback/
   https://yourdomain.com/accounts/apple/login/callback/
   ```

#### C. Generate Private Key
1. **Keys** → Buat baru
2. **Sign in with Apple** → Enable
3. Download `.p8` file
4. Convert ke format yang dibutuhkan

#### D. Tambah di Django Admin
1. **Social Applications** → **Add Social Application**
2. **Provider**: Apple
3. **Name**: Apple OAuth2
4. **Client id**: Service ID dari Apple
5. **Secret key**: Generated JWT token
6. **Key**: Team ID
7. **Sites**: Pilih "example.com"
8. **Save**

## Cara Akses Social Applications di Admin:

### Jika tidak melihat "Social Applications":

1. **Check INSTALLED_APPS** di `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...
       'allauth',
       'allauth.account', 
       'allauth.socialaccount',
       'allauth.socialaccount.providers.google',
       'allauth.socialaccount.providers.facebook',
       'allauth.socialaccount.providers.apple',
       # ...
   ]
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Restart server**:
   ```bash
   python manage.py runserver
   ```

### Lokasi di Django Admin:
- **SOCIAL ACCOUNTS** section
- **Social applications** (bukan "Social accounts")
- **Social application tokens**

## Testing OAuth2:

### 1. Dengan Test Credentials (Development):
```python
# settings.py - untuk testing
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'test-google-client-id',
            'secret': 'test-google-secret',
        }
    }
}
```

### 2. Test Login Flow:
1. Buka: http://localhost:8000/auth/login/
2. Klik tombol "Login with Google/Facebook/Apple"
3. Akan redirect ke provider OAuth2
4. Setelah authorize, kembali ke aplikasi

## Troubleshooting:

### Error "Social application not found":
- Pastikan Social Application sudah dibuat di admin
- Check Provider name exact match
- Pastikan Site sudah di-assign

### Error "Invalid redirect URI":
- Check exact URL di provider settings
- Pastikan include trailing slash `/`
- Check protokol HTTP vs HTTPS

### Error "Client ID not found":
- Pastikan credentials correct di Django admin
- Check provider configuration di settings.py

## Quick Setup Script:

Buat management command untuk auto-setup:

```python
# management/commands/setup_oauth.py
from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

class Command(BaseCommand):
    def handle(self, *args, **options):
        site = Site.objects.get_current()
        
        # Google
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            name='Google OAuth2',
            defaults={
                'client_id': 'your-google-client-id',
                'secret': 'your-google-secret',
            }
        )
        google_app.sites.add(site)
        
        # Facebook  
        facebook_app, created = SocialApp.objects.get_or_create(
            provider='facebook',
            name='Facebook OAuth2',
            defaults={
                'client_id': 'your-facebook-app-id',
                'secret': 'your-facebook-secret',
            }
        )
        facebook_app.sites.add(site)
        
        self.stdout.write('OAuth2 apps created successfully!')
```

Run dengan: `python manage.py setup_oauth`
