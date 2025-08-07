"""
Management command to debug static files and templates.
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.staticfiles import finders
from django.template.loader import get_template
import os


class Command(BaseCommand):
    help = 'Debug static files and template issues'

    def handle(self, *args, **options):
        self.stdout.write("=== Static Files Debug ===\n")
        
        # Check static configuration
        self.stdout.write(f"📁 STATIC_URL: {settings.STATIC_URL}")
        self.stdout.write(f"📁 STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
        self.stdout.write(f"📁 DEBUG: {settings.DEBUG}\n")
        
        # Check if key static files exist
        static_files = [
            'css/style.css',
            'css/bootstrap.min.css',
            'images/logo.svg',
            'images/login.jpg',
            'images/google.svg',
            'js/bootstrap.bundle.min.js',
        ]
        
        self.stdout.write("📦 Static files status:")
        for file_path in static_files:
            found = finders.find(file_path)
            status = "✅" if found else "❌"
            self.stdout.write(f"  {status} {file_path}")
            if found:
                self.stdout.write(f"      Found at: {found}")
        
        self.stdout.write("")
        
        # Check templates
        templates = [
            'layout/auth_base.html',
            'authentication/login.html',
            'authentication/register.html',
        ]
        
        self.stdout.write("📄 Template files status:")
        for template_name in templates:
            try:
                template = get_template(template_name)
                self.stdout.write(f"  ✅ {template_name}")
            except Exception as e:
                self.stdout.write(f"  ❌ {template_name}")
                self.stdout.write(f"      Error: {str(e)}")
        
        self.stdout.write("")
        
        # Check actual file paths
        if settings.STATICFILES_DIRS:
            static_dir = settings.STATICFILES_DIRS[0]
            self.stdout.write(f"📂 Checking static directory: {static_dir}")
            
            if os.path.exists(static_dir):
                self.stdout.write("  ✅ Static directory exists")
                
                # Check subdirectories
                subdirs = ['css', 'js', 'images']
                for subdir in subdirs:
                    full_path = os.path.join(static_dir, subdir)
                    if os.path.exists(full_path):
                        files_count = len(os.listdir(full_path))
                        self.stdout.write(f"    ✅ {subdir}/ ({files_count} files)")
                    else:
                        self.stdout.write(f"    ❌ {subdir}/ (not found)")
            else:
                self.stdout.write("  ❌ Static directory does not exist!")
        
        self.stdout.write("\n=== Recommendations ===")
        
        # Check for common issues
        missing_files = [f for f in static_files if not finders.find(f)]
        if missing_files:
            self.stdout.write(f"⚠️  Missing {len(missing_files)} static files:")
            for file_path in missing_files:
                self.stdout.write(f"   - {file_path}")
            
            if 'css/bootstrap.min.css' in missing_files:
                self.stdout.write("\n💡 Bootstrap CSS missing. Solutions:")
                self.stdout.write("   1. Download Bootstrap CSS to assets/css/")
                self.stdout.write("   2. Use CDN (already implemented in auth_base.html)")
                
        self.stdout.write("\n🔧 Quick fixes:")
        self.stdout.write("1. Collect static files: python manage.py collectstatic")
        self.stdout.write("2. Check file permissions in assets directory")
        self.stdout.write("3. Restart Django server")
        self.stdout.write("4. Clear browser cache")
        
        self.stdout.write("\n🌐 Test URLs:")
        self.stdout.write("- Login: http://localhost:8000/auth/login/")
        self.stdout.write("- Test: http://localhost:8000/auth/test-login/")
        self.stdout.write("- Admin: http://localhost:8000/admin/")
