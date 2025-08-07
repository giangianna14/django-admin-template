# OAuth2 Setup Guide

## Overview
This Django project now includes OAuth2 authentication with support for Google, Facebook, and Apple login using `django-allauth`.

## Features Added
- ✅ Login with Google OAuth2
- ✅ Login with Facebook OAuth2  
- ✅ Login with Apple OAuth2
- ✅ Email/Password authentication
- ✅ Password reset functionality
- ✅ User registration
- ✅ Social account connections management

## Setup Instructions

### 1. Google OAuth2 Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Go to "Credentials" → "Create Credentials" → "OAuth 2.0 Client IDs"
5. Set authorized redirect URIs:
   ```
   http://localhost:8000/accounts/google/login/callback/
   https://yourdomain.com/accounts/google/login/callback/
   ```
6. Copy Client ID and Client Secret
7. Update `settings.py`:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'APP': {
               'client_id': 'your-google-client-id',
               'secret': 'your-google-client-secret',
           }
       }
   }
   ```

### 2. Facebook OAuth2 Setup

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create a new app
3. Add "Facebook Login" product
4. Set valid OAuth redirect URIs:
   ```
   http://localhost:8000/accounts/facebook/login/callback/
   https://yourdomain.com/accounts/facebook/login/callback/
   ```
5. Copy App ID and App Secret
6. Update `settings.py`:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'facebook': {
           'APP': {
               'client_id': 'your-facebook-app-id',
               'secret': 'your-facebook-app-secret',
           }
       }
   }
   ```

### 3. Apple OAuth2 Setup

1. Go to [Apple Developer](https://developer.apple.com/)
2. Create App ID and Service ID
3. Configure Sign in with Apple
4. Generate private key and download
5. Set return URLs:
   ```
   http://localhost:8000/accounts/apple/login/callback/
   https://yourdomain.com/accounts/apple/login/callback/
   ```
6. Update `settings.py`:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'apple': {
           'APP': {
               'client_id': 'your-apple-service-id',
               'secret': 'your-apple-client-secret',
               'key': 'your-apple-team-id',
           }
       }
   }
   ```

### 4. Database Migration

Run migrations to create allauth tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## Testing OAuth2

1. Start development server:
   ```bash
   python manage.py runserver
   ```

2. Visit login page: http://localhost:8000/auth/login/

3. You'll see social login buttons for Google, Facebook, and Apple

4. Traditional email/password login is also available

## URLs Available

- `/auth/login/` - Login page with social auth
- `/auth/register/` - Registration page with social auth
- `/auth/password-reset/` - Password reset request
- `/auth/logout/` - Logout
- `/accounts/google/login/` - Direct Google login
- `/accounts/facebook/login/` - Direct Facebook login
- `/accounts/apple/login/` - Direct Apple login

## Email Configuration

For password reset emails to work, configure email settings in `settings.py`:

```python
# Email settings (for development, use console backend)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For production, use SMTP:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'
# DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

## Security Notes

1. **Never commit OAuth2 secrets to version control**
2. Use environment variables for production:
   ```python
   import os
   
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'APP': {
               'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
               'secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
           }
       }
   }
   ```

3. **Set proper redirect URIs** for each environment

4. **Enable HTTPS** in production

## Troubleshooting

### Common Issues:

1. **"Invalid redirect URI"**
   - Check OAuth2 app settings
   - Ensure exact URL match including trailing slashes

2. **"Social account not found"**
   - Run migrations: `python manage.py migrate`
   - Check app is in `INSTALLED_APPS`

3. **"Template not found"**
   - Ensure templates are in correct directory
   - Check `TEMPLATES` setting in `settings.py`

### Debug Mode:

Enable debug logging for allauth:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'allauth': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

## Production Checklist

- [ ] Set up HTTPS
- [ ] Configure OAuth2 apps for production domain
- [ ] Set up proper email backend
- [ ] Use environment variables for secrets
- [ ] Enable rate limiting
- [ ] Configure CSRF settings
- [ ] Set up monitoring and logging

## Support

For issues with specific OAuth2 providers:
- [Google OAuth2 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [Facebook Login Documentation](https://developers.facebook.com/docs/facebook-login/)
- [Apple Sign-in Documentation](https://developer.apple.com/sign-in-with-apple/)
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/)
