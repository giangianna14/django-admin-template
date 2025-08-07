"""
Management command to setup initial data for the project.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ecommerce.models import Category, Product, Customer


class Command(BaseCommand):
    """Setup initial data command."""
    help = 'Setup initial data for the Django admin template'

    def handle(self, *args, **options):
        """Handle the command."""
        self.stdout.write(self.style.SUCCESS('Setting up initial data...'))
        
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))
        
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic products and gadgets'},
            {'name': 'Clothing', 'description': 'Fashion and clothing items'},
            {'name': 'Books', 'description': 'Books and educational materials'},
            {'name': 'Home & Garden', 'description': 'Home improvement and garden items'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Category created: {category.name}')
        
        # Create sample products
        if Product.objects.count() == 0:
            electronics = Category.objects.get(name='Electronics')
            
            products_data = [
                {
                    'name': 'Smartphone XY',
                    'description': 'Latest smartphone with advanced features',
                    'price': 599.99,
                    'stock_quantity': 50,
                    'category': electronics
                },
                {
                    'name': 'Laptop Pro',
                    'description': 'High-performance laptop for professionals',
                    'price': 1299.99,
                    'stock_quantity': 20,
                    'category': electronics
                },
            ]
            
            for prod_data in products_data:
                Product.objects.create(**prod_data)
                self.stdout.write(f'Product created: {prod_data["name"]}')
        
        self.stdout.write(self.style.SUCCESS('Initial data setup completed!'))
