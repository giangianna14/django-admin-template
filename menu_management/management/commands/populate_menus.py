"""
Management command to populate menu data from existing sidebar structure.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from menu_management.models import MenuCategory, MenuItem, MenuSettings


class Command(BaseCommand):
    help = 'Populate menu management with existing sidebar structure'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Reset existing menu data before populating',
        )

    def handle(self, *args, **options):
        if options['reset']:
            self.stdout.write('Resetting existing menu data...')
            MenuItem.objects.all().delete()
            MenuCategory.objects.all().delete()

        # Create categories
        categories_data = [
            {'name': 'MAIN', 'slug': 'main', 'category_type': 'main', 'order': 1},
            {'name': 'APPS', 'slug': 'apps', 'category_type': 'apps', 'order': 2},
            {'name': 'PAGES', 'slug': 'pages', 'category_type': 'pages', 'order': 3},
            {'name': 'MODULES', 'slug': 'modules', 'category_type': 'modules', 'order': 4},
            {'name': 'OTHERS', 'slug': 'others', 'category_type': 'others', 'order': 5},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = MenuCategory.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Main menu items
        main_menus = [
            {
                'title': 'Dashboard',
                'slug': 'dashboard',
                'category': categories['main'],
                'menu_type': 'dropdown',
                'icon': 'dashboard',
                'order': 1,
                'children': [
                    {'title': 'eCommerce', 'slug': 'ecommerce-dashboard', 'url_name': '/dashboard', 'url_pattern': '/dashboard/', 'order': 1},
                    {'title': 'CRM', 'slug': 'crm-dashboard', 'url_name': '/crm', 'url_pattern': '/crm/', 'badge_text': 'Hot', 'order': 2},
                    {'title': 'Project Management', 'slug': 'project-management-dashboard', 'url_name': '/project-management', 'url_pattern': '/project-management/', 'order': 3},
                    {'title': 'LMS', 'slug': 'lms-dashboard', 'url_name': '/lms', 'url_pattern': '/lms/', 'order': 4},
                    {'title': 'HelpDesk', 'slug': 'help-desk-dashboard', 'url_name': '/help-desk', 'url_pattern': '/help-desk/', 'order': 5},
                    {'title': 'Analytics', 'slug': 'analytics-dashboard', 'url_name': '/analytics', 'url_pattern': '/analytics/', 'order': 6},
                    {'title': 'Crypto', 'slug': 'crypto-dashboard', 'url_name': '/crypto', 'url_pattern': '/crypto/', 'order': 7},
                    {'title': 'Sales', 'slug': 'sales-dashboard', 'url_name': '/sales', 'url_pattern': '/sales/', 'order': 8},
                    {'title': 'Hospital', 'slug': 'hospital-dashboard', 'url_name': '/hospital', 'url_pattern': '/hospital/', 'order': 9},
                    {'title': 'Marketing', 'slug': 'marketing-dashboard', 'url_name': '/marketing', 'url_pattern': '/marketing/', 'badge_text': 'New', 'order': 10},
                    {'title': 'NFT', 'slug': 'nft-dashboard', 'url_name': '/nft', 'url_pattern': '/nft/', 'badge_text': 'New', 'order': 11},
                    {'title': 'SaaS', 'slug': 'saas-dashboard', 'url_name': '/saas', 'url_pattern': '/saas/', 'badge_text': 'New', 'order': 12},
                    {'title': 'Real Estate', 'slug': 'real-estate-dashboard', 'url_name': '/real-estate', 'url_pattern': '/real-estate/', 'badge_text': 'New', 'order': 13},
                    {'title': 'Shipment', 'slug': 'shipment-dashboard', 'url_name': '/shipment', 'url_pattern': '/shipment/', 'badge_text': 'New', 'order': 14},
                    {'title': 'Finance', 'slug': 'finance-dashboard', 'url_name': '/finance', 'url_pattern': '/finance/', 'badge_text': 'New', 'order': 15},
                    {'title': 'HRM', 'slug': 'hrm-dashboard', 'url_name': '/hrm', 'url_pattern': '/hrm/', 'badge_text': 'New', 'order': 16},
                    {'title': 'School', 'slug': 'school-dashboard', 'url_name': '/school', 'url_pattern': '/school/', 'badge_text': 'New', 'order': 17},
                    {'title': 'Call Center', 'slug': 'call-center-dashboard', 'url_name': '/call-center', 'url_pattern': '/call-center/', 'badge_text': 'New', 'order': 18},
                    {'title': 'POS System', 'slug': 'pos-system-dashboard', 'url_name': '/pos-system', 'url_pattern': '/pos-system/', 'badge_text': 'New', 'order': 19},
                    {'title': 'Podcast', 'slug': 'podcast-dashboard', 'url_name': '/podcast', 'url_pattern': '/podcast/', 'badge_text': 'New', 'order': 20},
                    {'title': 'Social Media', 'slug': 'social-media-dashboard', 'url_name': '/social-media', 'url_pattern': '/social-media/', 'badge_text': 'New', 'order': 21},
                ]
            },
            {
                'title': 'Front Pages',
                'slug': 'front-pages',
                'category': categories['main'],
                'menu_type': 'dropdown',
                'icon': 'note_stack',
                'order': 2,
                'children': [
                    {'title': 'Home', 'slug': 'home', 'url_name': '/', 'url_pattern': '/', 'order': 1},
                    {'title': 'Features', 'slug': 'features', 'url_name': '/features', 'url_pattern': '/features', 'order': 2},
                    {'title': 'Our Team', 'slug': 'our-team', 'url_name': '/our-team', 'url_pattern': '/our-team', 'order': 3},
                    {'title': "FAQ's", 'slug': 'faqs', 'url_name': '/faqs', 'url_pattern': '/faqs', 'order': 4},
                    {'title': 'Contact', 'slug': 'contact', 'url_name': '/contact', 'url_pattern': '/contact', 'order': 5},
                ]
            }
        ]

        # Apps menu items
        apps_menus = [
            {'title': 'Calendar', 'slug': 'calendar', 'category': categories['apps'], 'url_name': '/calendar', 'url_pattern': '/calendar/', 'icon': 'date_range', 'order': 1},
            {'title': 'To Do List', 'slug': 'to-do-list', 'category': categories['apps'], 'url_name': '/to-do-list', 'url_pattern': '/to-do-list/', 'icon': 'format_list_bulleted', 'order': 2},
            {'title': 'Contacts', 'slug': 'contacts', 'category': categories['apps'], 'url_name': '/contacts', 'url_pattern': '/contacts/', 'icon': 'contact_page', 'order': 3},
            {'title': 'Chat', 'slug': 'chat', 'category': categories['apps'], 'url_name': '/chat', 'url_pattern': '/chat/', 'icon': 'chat', 'order': 4},
            {'title': 'Kanban Board', 'slug': 'kanban-board', 'category': categories['apps'], 'url_name': '/kanban-board', 'url_pattern': '/kanban-board/', 'icon': 'space_dashboard', 'order': 6},
        ]

        # Create menu items
        def create_menu_item(menu_data, parent=None):
            children_data = menu_data.pop('children', [])
            menu_item, created = MenuItem.objects.get_or_create(
                slug=menu_data['slug'],
                parent=parent,
                defaults=menu_data
            )
            if created:
                self.stdout.write(f'Created menu item: {menu_item.title}')
            
            # Create children
            for child_data in children_data:
                child_data['category'] = menu_data['category']
                create_menu_item(child_data, parent=menu_item)
            
            return menu_item

        # Create main menus
        for menu_data in main_menus:
            create_menu_item(menu_data)

        # Create apps menus
        for menu_data in apps_menus:
            create_menu_item(menu_data)

        # Create menu settings
        settings, created = MenuSettings.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'Trezo',
                'logo_icon': '/static/images/logo-icon.png',
                'menu_style': 'sidebar',
                'show_menu_icons': True,
                'show_menu_badges': True,
                'auto_close_dropdowns': True,
                'highlight_active_menu': True,
            }
        )
        if created:
            self.stdout.write('Created menu settings')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated menu management data!')
        )
