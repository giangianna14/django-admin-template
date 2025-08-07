#!/usr/bin/env python
"""
Script untuk menguji halaman profile dengan data user yang sebenarnya
"""
import os
import sys
import django
from django.contrib.auth.models import User
from django.test import Client

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')
django.setup()

def test_profile_page():
    print("🔍 Testing Profile Page...")
    
    # Create test client
    client = Client()
    
    # Check if there are any users
    users = User.objects.all()
    print(f"📊 Total users in database: {users.count()}")
    
    if users.exists():
        # Get first user
        user = users.first()
        print(f"👤 Testing with user: {user.username}")
        print(f"📧 Email: {user.email}")
        print(f"📅 Date joined: {user.date_joined}")
        print(f"🔑 User ID: {user.id}")
        print(f"👨‍💼 Full name: {user.get_full_name() or 'Not set'}")
        print(f"✅ Is active: {user.is_active}")
        print(f"🔒 Is staff: {user.is_staff}")
        print(f"⭐ Is superuser: {user.is_superuser}")
        
        # Login the user
        client.force_login(user)
        
        # Test profile page
        response = client.get('/my-profile/')
        print(f"🌐 Profile page status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Profile page loaded successfully!")
            print("🎯 Template context variables that will be available:")
            print(f"   - user.username: {user.username}")
            print(f"   - user.email: {user.email}")
            print(f"   - user.get_full_name: {user.get_full_name() or 'Not set'}")
            print(f"   - user.first_name: {user.first_name or 'Not set'}")
            print(f"   - user.last_name: {user.last_name or 'Not set'}")
            print(f"   - user.date_joined: {user.date_joined.strftime('%d %b %Y')}")
            print(f"   - user.last_login: {user.last_login.strftime('%d %b %Y %H:%M') if user.last_login else 'Never'}")
            print(f"   - user.id: {user.id}")
            print(f"   - user.is_active: {user.is_active}")
            print(f"   - Account type: {'Administrator' if user.is_superuser else 'Staff' if user.is_staff else 'Regular User'}")
        else:
            print(f"❌ Error loading profile page: {response.status_code}")
            
    else:
        print("⚠️  No users found in database")
        print("💡 Create a user first by registering at: http://127.0.0.1:8000/register/")
    
    print("\n🚀 You can now access the profile page at: http://127.0.0.1:8000/my-profile/")
    print("📝 Make sure you're logged in first!")

if __name__ == "__main__":
    test_profile_page()
