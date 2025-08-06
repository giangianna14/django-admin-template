#!/usr/bin/env python3

import os
import sys
import django
from django.template.loader import render_to_string
from django.test import RequestFactory

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')
django.setup()

def test_template_rendering():
    """Test rendering template untuk memastikan tidak ada error URL"""
    try:
        factory = RequestFactory()
        request = factory.get('/login/')
        
        # Test rendering login template
        html = render_to_string('login.html', {}, request=request)
        print("✅ Template login.html berhasil di-render")
        
        # Test rendering allauth login template
        html = render_to_string('account/login.html', {}, request=request)
        print("✅ Template account/login.html berhasil di-render")
        
        print("🚀 Semua template berhasil di-render tanpa error!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_template_rendering()
