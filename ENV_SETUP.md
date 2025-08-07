# Environment Variables Configuration Guide

## Overview

Your Django project now uses environment variables for configuration management, making it more secure and flexible for different deployment environments.

## ✅ Files Created

1. **`.env`** - Your local environment variables (already configured)
2. **`.env.example`** - Template for new developers
3. **Updated `settings.py`** - Now reads from environment variables
4. **Updated `requirements.txt`** - Includes `python-decouple`

## 🔧 How It Works

The project uses `python-decouple` library to read environment variables from the `.env` file. This provides:

- **Security**: Sensitive data (like SECRET_KEY) is not in version control
- **Flexibility**: Different settings for development, staging, production
- **Portability**: Easy to deploy to different environments

## 📝 Environment Variables Explained

### Core Django Settings
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

### Database Configuration
```env
DATABASE_URL=sqlite:///db.sqlite3
```
*For production, change to PostgreSQL/MySQL URL*

### Localization
```env
TIME_ZONE=Asia/Jakarta
LANGUAGE_CODE=id-id
```

### File Uploads
```env
FILE_UPLOAD_MAX_MEMORY_SIZE=5242880
DATA_UPLOAD_MAX_MEMORY_SIZE=5242880
```
*Values in bytes (5MB = 5242880 bytes)*

### Email Settings
```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Social Authentication (Optional)
```env
GOOGLE_OAUTH2_KEY=your-google-oauth2-key
GOOGLE_OAUTH2_SECRET=your-google-oauth2-secret
```

## 🚀 Development Setup

### For New Developers:

1. **Copy the template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit values:**
   ```bash
   nano .env
   ```

3. **Required changes:**
   - Generate a new `SECRET_KEY` for security
   - Set your email credentials (if using email features)
   - Configure social auth keys (if using OAuth)

## 🛡️ Security Best Practices

### ✅ Do:
- Keep `.env` file in `.gitignore` (already done)
- Use strong, unique SECRET_KEY for each environment
- Set `DEBUG=False` in production
- Restrict `ALLOWED_HOSTS` in production

### ❌ Don't:
- Commit `.env` file to version control
- Use default SECRET_KEY in production
- Leave DEBUG=True in production
- Use weak passwords for database/email

## 🌍 Production Deployment

### 1. Environment Variables
```env
DEBUG=False
SECRET_KEY=your-strong-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### 2. Security Settings
```env
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
X_FRAME_OPTIONS=DENY
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

### 3. Email Configuration (Production)
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=noreply@yourdomain.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

## 🔧 Advanced Configuration

### Database URLs Examples

**SQLite (Development):**
```env
DATABASE_URL=sqlite:///db.sqlite3
```

**PostgreSQL (Production):**
```env
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

**MySQL (Production):**
```env
DATABASE_URL=mysql://user:password@localhost:3306/dbname
```

### Logging Configuration
```env
LOG_LEVEL=DEBUG    # Development
LOG_LEVEL=INFO     # Production
LOG_LEVEL=ERROR    # Production (minimal)
```

## 🐛 Troubleshooting

### Common Issues:

1. **"config not found" error:**
   - Ensure `.env` file exists in project root
   - Check file permissions

2. **"Invalid literal for int()" error:**
   - Remove comments from numeric values in .env
   - Example: Use `FILE_UPLOAD_MAX_MEMORY_SIZE=5242880` not `5242880 # 5MB`

3. **"ModuleNotFoundError: decouple":**
   - Install python-decouple: `pip install python-decouple`

4. **Settings not loading:**
   - Restart Django server after changing .env
   - Check file encoding (should be UTF-8)

## 📚 Additional Resources

- [Python Decouple Documentation](https://github.com/henriquebastos/python-decouple)
- [Django Settings Documentation](https://docs.djangoproject.com/en/stable/topics/settings/)
- [12-Factor App Methodology](https://12factor.net/)

## ✅ Verification

To verify your environment is working correctly:

```bash
# Check Django configuration
python manage.py check

# Show current settings (development only)
python manage.py shell -c "from django.conf import settings; print(f'DEBUG: {settings.DEBUG}'); print(f'SECRET_KEY: {settings.SECRET_KEY[:10]}...')"

# Test database connection
python manage.py migrate --dry-run
```

---

**Your Django project is now configured with environment variables! 🎉**

This makes your application more secure, flexible, and ready for professional deployment.
