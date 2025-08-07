# Django Admin Template - Modular Structure with OAuth2

A comprehensive Django admin template with OAuth2 authentication, clean modular architecture, and app-specific template organization. This project provides a robust foundation for building modern admin dashboards with multiple business modules.

## 🏗️ Project Structure

```
django-admin-template/
├── authentication/           # User authentication & OAuth2
│   ├── templates/authentication/    # Auth-specific templates
│   ├── management/commands/         # Custom Django commands
│   └── views.py              # Authentication views with OAuth2
├── core/                     # Core pages (home, features, contact)
│   └── templates/core/       # Core page templates
├── dashboard/                # Various dashboard types
│   └── templates/dashboard/  # Dashboard templates
├── ecommerce/                # E-commerce functionality
│   └── templates/ecommerce/  # E-commerce templates
├── communication/            # Email, chat, calendar
│   └── templates/communication/  # Communication templates
├── ui_components/            # UI elements & components
│   └── templates/ui_components/  # Component templates
├── project_management/       # Project management features
│   └── templates/project_management/  # Project templates
├── file_management/          # File handling features
│   └── templates/file_management/    # File management templates
├── lms/                      # Learning Management System
│   └── templates/lms/        # LMS templates
├── events/                   # Event management
│   └── templates/events/     # Event templates
├── invoicing/                # Invoice management
│   └── templates/invoicing/  # Invoice templates
├── support/                  # Help desk & support
│   └── templates/support/    # Support templates
├── user_management/          # User administration
│   └── templates/user_management/   # User management templates
├── my_app/                   # Main Django project
│   ├── templates/layout/     # Shared layout templates
│   ├── templates/shared/     # Common components
│   └── assets/               # Static assets (CSS, JS, images)
└── .vscode/                  # VS Code configuration
```

## 🚀 Features

### Core Features
- **OAuth2 Authentication**: Google, Facebook, Apple social login
- **Modular Architecture**: Clean separation of concerns with app-specific templates
- **Authentication System**: Complete user management with social login
- **Multiple Dashboards**: E-commerce, CRM, Analytics, Finance, HRM, etc.
- **UI Components**: Comprehensive component library
- **Responsive Design**: Mobile-first Bootstrap approach

### OAuth2 Integration
- **Google OAuth2**: Seamless Google account integration
- **Facebook OAuth2**: Facebook social login
- **Apple OAuth2**: Apple ID authentication
- **Django Allauth**: Comprehensive social authentication framework
- **Custom Templates**: Beautiful, branded login/register pages

### Business Modules
- **E-commerce**: Products, orders, customers, sellers, cart functionality
- **Project Management**: Projects, tasks, teams, Kanban boards
- **Communication**: Email, chat, calendar, contacts, inbox management
- **File Management**: Document handling, file organization
- **Learning Management System (LMS)**: Courses, instructors, lessons
- **Event Management**: Event creation, scheduling, management
- **Invoicing**: Invoice creation, management, tracking
- **Support & Help Desk**: Ticket management, agent dashboard
- **User Management**: User administration, profiles, permissions
- **Analytics**: Various dashboard types (CRM, Finance, HRM, etc.)

### Technical Features
- **Django 5.2.5**: Latest Django framework
- **Django Allauth 65.10.0**: Social authentication framework
- **OAuth2 Integration**: Google, Facebook, Apple login
- **App-specific Templates**: Each module manages its own templates
- **Class-based Views**: Clean view architecture
- **Model Relationships**: Proper database design
- **Admin Interface**: Custom admin configurations
- **Static Files**: Organized asset management
- **Chrome Integration**: VS Code Chrome browser support

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-admin-template
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Create superuser and sample data**
   ```bash
   python3 manage.py setup_data
   ```

6. **Configure OAuth2 (Optional)**
   - Set up Google OAuth2 credentials in Django admin
   - Configure Facebook App ID and secret
   - Set up Apple OAuth2 configuration
   - Update `my_app/settings.py` with your OAuth2 credentials

7. **Run development server**
   ```bash
   python3 manage.py runserver
   ```

## 🔐 OAuth2 Setup

### Google OAuth2
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth2 credentials
5. Add authorized redirect URIs:
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
   - `http://localhost:8000/accounts/google/login/callback/`
6. Update settings with your Client ID and Secret

### Facebook OAuth2
1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create a new app
3. Add Facebook Login product
4. Configure Valid OAuth Redirect URIs:
   - `http://127.0.0.1:8000/accounts/facebook/login/callback/`
5. Update settings with your App ID and Secret

### Apple OAuth2
1. Go to [Apple Developer Console](https://developer.apple.com/)
2. Create a new Service ID
3. Configure Sign In with Apple
4. Update settings with your credentials

## 🎯 Usage

### URL Structure

```
/ (root)                      # Core pages
├── auth/                     # Custom Authentication
│   ├── login/                # Beautiful OAuth2 login page
│   ├── register/             # Social registration
│   ├── forget-password/      # Password reset
│   └── profile/              # User profile
├── accounts/                 # Django Allauth URLs
│   ├── google/login/         # Google OAuth2
│   ├── facebook/login/       # Facebook OAuth2
│   └── apple/login/          # Apple OAuth2
├── dashboard/                # Dashboard pages
│   ├── analytics/            # Analytics dashboard
│   ├── crm/                  # CRM dashboard
│   ├── ecommerce/            # E-commerce dashboard
│   ├── finance/              # Finance dashboard
│   └── hrm/                  # HRM dashboard
├── ecommerce/               # E-commerce features
│   ├── products-list/
│   ├── orders/
│   ├── customers/
│   └── cart/
├── communication/           # Communication tools
│   ├── inbox/
│   ├── chat/
│   ├── calendar/
│   └── contacts/
├── lms/                     # Learning Management
│   ├── courses-list/
│   ├── instructors/
│   └── course-details/
├── events/                  # Event Management
│   ├── events-list/
│   ├── create-an-event/
│   └── event-details/
├── projects/                # Project Management
│   ├── project-list/
│   ├── kanban-board/
│   └── teams/
└── components/              # UI components
    ├── alerts/
    ├── buttons/
    └── sweet-alarts/
```

### Key Views

**Authentication with OAuth2**
- Beautiful login page with social buttons
- Registration with OAuth2 integration
- Password management
- User profiles
- Social account connections

**Dashboard Collection**
- Analytics dashboard with charts
- E-commerce dashboard
- CRM dashboard with customer insights
- Finance dashboard
- HRM dashboard
- Hospital dashboard
- Marketing dashboard
- And many more specialized dashboards

**E-commerce Suite**
- Product management (create, edit, list)
- Order processing and tracking
- Customer management
- Seller management
- Shopping cart functionality
- Review and rating system

**Communication Hub**
- Email management (inbox, sent, draft)
- Real-time chat interface
- Calendar with event scheduling
- Contact management
- To-do list functionality

**Learning Management System**
- Course creation and management
- Instructor profiles
- Lesson planning
- Student enrollment

**Project Management**
- Project creation and tracking
- Kanban board interface
- Team management
- Client management

**File Management**
- Document organization
- File upload and storage
- Media management
- Application file handling

## 🔧 Configuration

### Settings Structure
- Development settings in `my_app/settings.py`
- Static files configuration
- Template directories
- Database configuration

### Template Organization (New Structure)
- **App-specific templates**: Each Django app has its own `templates/app_name/` directory
- **Shared layouts**: Common layouts in `my_app/templates/layout/`
- **Namespace safety**: Templates are automatically namespaced by app name
- **Better maintainability**: Templates are logically grouped with their functionality
- **Django best practices**: Follows modern Django template organization

### Template Migration Completed
- ✅ **200+ templates** moved to respective app directories
- ✅ **13 modules** now have organized template structure
- ✅ **Namespace conflicts** eliminated
- ✅ **Better modularity** achieved

### Static Assets
- CSS files in `my_app/assets/css/`
- JavaScript files in `my_app/assets/js/`
- Images in `my_app/assets/images/`

## 🛠️ Development

### Adding New Apps
1. Create new Django app: `python3 manage.py startapp new_app`
2. Add to `INSTALLED_APPS` in settings
3. Create URLs configuration
4. Create template directory: `new_app/templates/new_app/`
5. Update main URLs
6. Follow template naming conventions

### Creating Models
1. Define models in `models.py`
2. Create migrations: `python3 manage.py makemigrations`
3. Apply migrations: `python3 manage.py migrate`
4. Register in admin: `admin.py`

### Template Development
- **App templates**: Create in `app_name/templates/app_name/`
- **Base templates**: Extend from `layout/auth_base.html` or `layout/dashboard_base.html`
- **Shared components**: Use components from `my_app/templates/shared/`
- **Consistent naming**: Follow existing naming conventions

## 📱 Features by Module

### Core Module
- Homepage and landing pages
- Static content pages (about, contact, features)
- SEO-friendly structure
- Privacy policy and terms

### Authentication Module
- **OAuth2 Integration**: Google, Facebook, Apple
- User registration/login with social options
- Password reset functionality
- User profile management
- Permission-based access
- Beautiful, responsive login pages

### E-commerce Module
- Product catalog with grid/list views
- Shopping cart functionality
- Order management and tracking
- Customer profiles and management
- Seller management system
- Review and rating system
- Category management

### Communication Module
- Email management (inbox, sent, draft, spam)
- Real-time chat interface
- Calendar integration with events
- Contact management system
- To-do list functionality

### Dashboard Module
- **Analytics Dashboard**: Charts and metrics
- **E-commerce Dashboard**: Sales overview
- **CRM Dashboard**: Customer insights
- **Finance Dashboard**: Financial metrics
- **HRM Dashboard**: HR management
- **Hospital Dashboard**: Healthcare metrics
- **Marketing Dashboard**: Campaign analytics
- **And many more specialized dashboards**

### Learning Management System (LMS)
- Course creation and management
- Instructor profiles and management
- Lesson planning and delivery
- Student enrollment system
- Course progress tracking

### Project Management Module
- Project creation and tracking
- Kanban board interface
- Team management
- Client management
- Task assignment and tracking

### Event Management Module
- Event creation and scheduling
- Event details and management
- Event listing and filtering
- Calendar integration

### File Management Module
- Document organization
- File upload and storage
- Media management
- Application file handling
- Recent files tracking

### UI Components Module
- Comprehensive component library
- Alert systems and notifications
- Form components and validation
- Navigation elements
- Data visualization components
- Charts and graphs (Apex Charts)

### Invoicing Module
- Invoice creation and management
- Invoice templates
- Payment tracking
- Customer billing

### Support Module
- Ticket management system
- Agent dashboard
- Customer support interface
- Knowledge base

### User Management Module
- User administration
- Team member management
- User profiles and permissions
- Role-based access control

## 🔐 Security

- **CSRF protection** enabled for all forms
- **OAuth2 security** with proper token handling
- **Secure password** handling and hashing
- **User authentication** required for protected views
- **Permission-based** access control
- **Social account** security with django-allauth
- **Session management** and security

## 📊 Admin Interface

- Custom admin configurations for all modules
- Inline editing capabilities
- Advanced filtering and searching
- Bulk operations support
- OAuth2 social account management
- User permission management

## 🌐 Production Deployment

1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving (WhiteNoise or CDN)
4. Configure OAuth2 production credentials
5. Set up environment variables for sensitive data
6. Configure proper logging
7. Set up SSL/HTTPS for OAuth2 security

## 🆕 Recent Updates

### Template Organization (Latest)
- ✅ **Moved all templates** to respective app directories
- ✅ **200+ templates** organized by module
- ✅ **Improved maintainability** with app-specific templates
- ✅ **Django best practices** implementation
- ✅ **Namespace safety** for template resolution

### OAuth2 Integration (Latest)
- ✅ **Google OAuth2** fully implemented
- ✅ **Facebook OAuth2** ready for configuration
- ✅ **Apple OAuth2** ready for configuration
- ✅ **Beautiful login pages** with social buttons
- ✅ **Django Allauth** integration
- ✅ **Custom authentication** views

### VS Code Integration
- ✅ **Chrome browser** integration
- ✅ **VS Code tasks** for development
- ✅ **Development workflow** optimization

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Follow coding standards and Django best practices
4. Add tests if applicable
5. Update documentation
6. Submit pull request with detailed description

## 📚 Documentation

- **Template Migration**: See `TEMPLATE_MIGRATION_SUMMARY.md`
- **OAuth2 Setup**: See `OAUTH2_SETUP.md`
- **OAuth2 Admin**: See `OAUTH2_ADMIN_SETUP.md`
- **OAuth2 Ready**: See `OAUTH2_READY.md`

## 📄 License

This project is licensed under the MIT License. Feel free to use it for personal and commercial projects.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check existing documentation files
- Review existing issues and solutions
- Contact the development team

## 🔗 Quick Links

- **Live Demo**: [Coming Soon]
- **Documentation**: Check the `.md` files in the repository
- **Issues**: [GitHub Issues](https://github.com/your-username/django-admin-template/issues)
- **Contributing**: Follow the contribution guidelines above

---

**Note**: This is a comprehensive template project designed to be customized for specific business needs. The modular architecture allows you to use only the modules you need and extend with additional functionality as required.

**Latest Update**: Template organization completed with app-specific directories and OAuth2 integration fully functional.
