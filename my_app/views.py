from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import LoginForm, RegisterForm, ForgotPasswordForm, UserProfileForm, UserAccountForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html', {})

def features(request):
    return render(request, 'features.html', {})

def our_team(request):
    return render(request, 'our-team.html', {})

def faqs(request):
    return render(request, 'faqs.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                error = 'Username atau password salah.'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def register(request):
    error = None
    success = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            success = f'Akun untuk {username} berhasil dibuat! Silakan login.'
            return redirect('login')
        else:
            error = 'Ada kesalahan dalam form. Silakan periksa kembali.'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'error': error, 'success': success})

def forget_password(request):
    message = None
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Di sini Anda bisa menambahkan logika untuk mengirim email reset password
            message = f'Link reset password telah dikirim ke {email}'
    else:
        form = ForgotPasswordForm()
    return render(request, 'forget-password.html', {'form': form, 'message': message})

@login_required
def dashboard(request):
    return render(request, 'ecommerce.html', {})

def crm(request):
    return render(request, 'crm.html', {})

def project_management(request):
    return render(request, 'project-management.html', {})

def lms(request):
    return render(request, 'lms.html', {})

def help_desk(request):
    return render(request, 'help-desk.html', {})

def analytics(request):
    return render(request, 'analytics.html', {})

def crypto(request):
    return render(request, 'crypto.html', {})

def sales(request):
    return render(request, 'sales.html', {})

def hospital(request):
    return render(request, 'hospital.html', {})

def marketing(request):
    return render(request, 'marketing.html', {})

def nft(request):
    return render(request, 'nft.html', {})

def saas(request):
    return render(request, 'saas.html', {})

def real_estate(request):
    return render(request, 'real-estate.html', {})

def shipment(request):
    return render(request, 'shipment.html', {})

def finance(request):
    return render(request, 'finance.html', {})

def hrm(request):
    return render(request, 'hrm.html', {})

def school(request):
    return render(request, 'school.html', {})

def call_center(request):
    return render(request, 'call-center.html', {})

def pos_system(request):
    return render(request, 'pos-system.html', {})

def podcast(request):
    return render(request, 'podcast.html', {})

def social_media(request):
    return render(request, 'social-media.html', {})

def calendar(request):
    return render(request, 'calendar.html', {})

def to_do_list(request):
    return render(request, 'to-do-list.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def chat(request):
    return render(request, 'chat.html', {})

def inbox(request):
    return render(request, 'inbox.html', {})

def compose(request):
    return render(request, 'compose.html', {})

def read_email(request):
    return render(request, 'read-email.html', {})

def snoozed(request):
    return render(request, 'snoozed.html', {})

def draft(request):
    return render(request, 'draft.html', {})

def sent_mail(request):
    return render(request, 'sent-mail.html', {})

def trash_email(request):
    return render(request, 'trash-email.html', {})

def spam(request):
    return render(request, 'spam.html', {})

def starred(request):
    return render(request, 'starred.html', {})

def important(request):
    return render(request, 'important.html', {})

def kanban_board(request):
    return render(request, 'kanban-board.html', {})

def file_manager(request):
    return render(request, 'file-manager.html', {})

def assets(request):
    return render(request, 'assets.html', {})

def projects(request):
    return render(request, 'projects.html', {})

def personal(request):
    return render(request, 'personal.html', {})

def applications(request):
    return render(request, 'applications.html', {})

def documents(request):
    return render(request, 'documents.html', {})

def media(request):
    return render(request, 'media.html', {})

def recents(request):
    return render(request, 'recents.html', {})

def drive_important(request):
    return render(request, 'drive-important.html', {})

def drive_spam(request):
    return render(request, 'drive-spam.html', {})

def drive_trash(request):
    return render(request, 'drive-trash.html', {})

def products_grid(request):
    return render(request, 'products-grid.html', {})

def products_list(request):
    return render(request, 'products-list.html', {})

def product_details(request):
    return render(request, 'product-details.html', {})

def create_product(request):
    return render(request, 'create-product.html', {})

def edit_product(request):
    return render(request, 'edit-product.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def orders(request):
    return render(request, 'orders.html', {})

def order_details(request):
    return render(request, 'order-details.html', {})

def create_order(request):
    return render(request, 'create-order.html', {})

def order_tracking(request):
    return render(request, 'order-tracking.html', {})

def customers(request):
    return render(request, 'customers.html', {})

def customer_details(request):
    return render(request, 'customer-details.html', {})

def categories(request):
    return render(request, 'categories.html', {})

def sellers(request):
    return render(request, 'sellers.html', {})

def seller_details(request):
    return render(request, 'seller-details.html', {})

def create_seller(request):
    return render(request, 'create-seller.html', {})

def reviews(request):
    return render(request, 'reviews.html', {})

def refunds(request):
    return render(request, 'refunds.html', {})

def contacts_two(request):
    return render(request, 'contacts-2.html', {})

def customers_two(request):
    return render(request, 'customers-2.html', {})

def leads(request):
    return render(request, 'leads.html', {})

def deals(request):
    return render(request, 'deals.html', {})

def project_overview(request):
    return render(request, 'project-overview.html', {})

def project_list(request):
    return render(request, 'project-list.html', {})

def create_project(request):
    return render(request, 'create-project.html', {})

def clients(request):
    return render(request, 'clients.html', {})

def teams(request):
    return render(request, 'teams.html', {})

def kanban_board_two(request):
    return render(request, 'kanban-board-2.html', {})

def user(request):
    return render(request, 'user.html', {})

def courses_list(request):
    return render(request, 'courses-list.html', {})

def course_details(request):
    return render(request, 'course-details.html', {})

def lesson_preview(request):
    return render(request, 'lesson-preview.html', {})

def create_course(request):
    return render(request, 'create-course.html', {})

def edit_course(request):
    return render(request, 'edit-course.html', {})

def instructors(request):
    return render(request, 'instructors.html', {})

def tickets(request):
    return render(request, 'tickets.html', {})

def ticket_details(request):
    return render(request, 'ticket-details.html', {})

def agents(request):
    return render(request, 'agents.html', {})

def reports(request):
    return render(request, 'reports.html', {})

def starter(request):
    return render(request, 'starter.html', {})

def events(request):
    return render(request, 'events.html', {})

def events_list(request):
    return render(request, 'events-list.html', {})

def event_details(request):
    return render(request, 'event-details.html', {})

def create_an_event(request):
    return render(request, 'create-an-event.html', {})

def edit_an_event(request):
    return render(request, 'edit-an-event.html', {})

def profile(request):
    return render(request, 'profile.html', {})

@login_required
def settings(request):
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Handle form submission
        account_form = UserAccountForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        # Check which form was submitted
        if 'save_account' in request.POST:
            if account_form.is_valid():
                account_form.save()
                messages.success(request, 'Account information updated successfully!')
                return redirect('settings')
            else:
                messages.error(request, 'Please correct the errors below.')
        
        elif 'save_profile' in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile information updated successfully!')
                return redirect('settings')
            else:
                messages.error(request, 'Please correct the errors below.')
        
        elif 'delete_profile_picture' in request.POST:
            if profile.profile_picture:
                profile.profile_picture.delete()
                messages.success(request, 'Profile picture deleted successfully!')
            return redirect('settings')
        
        elif 'delete_cover_photo' in request.POST:
            if profile.cover_photo:
                profile.cover_photo.delete()
                messages.success(request, 'Cover photo deleted successfully!')
            return redirect('settings')
            
    else:
        # Initialize forms with current data
        account_form = UserAccountForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user': request.user,
        'profile': profile,
        'account_form': account_form,
        'profile_form': profile_form,
    }
    return render(request, 'settings.html', context)

def invoice_list(request):
    return render(request, 'invoice-list.html', {})

def invoice_details(request):
    return render(request, 'invoice-details.html', {})

def create_invoice(request):
    return render(request, 'create-invoice.html', {})

def edit_invoice(request):
    return render(request, 'edit-invoice.html', {})

def team_members(request):
    return render(request, 'team-members.html', {})

def users_list(request):
    return render(request, 'users-list.html', {})

def add_user(request):
    return render(request, 'add-user.html', {})

def user_profile(request):
    return render(request, 'user-profile.html', {})

def teams_two(request):
    return render(request, 'teams-2.html', {})

def my_projects(request):
    return render(request, 'my-projects.html', {})

@login_required
def my_profile(request):
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'my-profile.html', context)

def material_icons(request):
    return render(request, 'material-icons.html', {})

def feathericon(request):
    return render(request, 'feathericon.html', {})

def remixicon(request):
    return render(request, 'remixicon.html', {})

def alerts(request):
    return render(request, 'alerts.html', {})

def avatar(request):
    return render(request, 'avatar.html', {})

def buttons(request):
    return render(request, 'buttons.html', {})

def badges(request):
    return render(request, 'badges.html', {})

def cards(request):
    return render(request, 'cards.html', {})

def carousels(request):
    return render(request, 'carousels.html', {})

def dropdowns(request):
    return render(request, 'dropdowns.html', {})

def grids(request):
    return render(request, 'grids.html', {})

def images(request):
    return render(request, 'images.html', {})

def list(request):
    return render(request, 'list.html', {})

def modals(request):
    return render(request, 'modals.html', {})

def navs(request):
    return render(request, 'navs.html', {})

def paginations(request):
    return render(request, 'paginations.html', {})

def popover_tooltips(request):
    return render(request, 'popover-tooltips.html', {})

def progress(request):
    return render(request, 'progress.html', {})

def spinners(request):
    return render(request, 'spinners.html', {})

def tabs(request):
    return render(request, 'tabs.html', {})

def accordions(request):
    return render(request, 'accordions.html', {})

def date_time_picker(request):
    return render(request, 'date-time-picker.html', {})

def videos(request):
    return render(request, 'videos.html', {})

def basic_table(request):
    return render(request, 'basic-table.html', {})

def data_tables(request):
    return render(request, 'data-tables.html', {})

def basic_elements(request):
    return render(request, 'basic-elements.html', {})

def advanced_elements(request):
    return render(request, 'advanced-elements.html', {})

def validation(request):
    return render(request, 'validation.html', {})

def wizard(request):
    return render(request, 'wizard.html', {})

def editors(request):
    return render(request, 'editors.html', {})

def file_upload(request):
    return render(request, 'file-upload.html', {})

def apex_charts(request):
    return render(request, 'apex-charts.html', {})

def reset_password(request):
    return render(request, 'reset-password.html', {})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Anda berhasil logout.')
    return redirect('login')

def confirm_mail(request):
    return render(request, 'confirm-mail.html', {})

def pricing_plan(request):
    return render(request, 'pricing-plan.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def timeline(request):
    return render(request, 'timeline.html', {})

def animation(request):
    return render(request, 'animation.html', {})

def clip_board(request):
    return render(request, 'clip-board.html', {})

def drag_drop(request):
    return render(request, 'drag-drop.html', {})

def range_slider(request):
    return render(request, 'range-slider.html', {})

def ratings(request):
    return render(request, 'ratings.html', {})

def toasts(request):
    return render(request, 'toasts.html', {})

def check_radio(request):
    return render(request, 'check-radio.html', {})

def sweet_alarts(request):
    return render(request, 'sweet-alarts.html', {})

def select(request):
    return render(request, 'select.html', {})

def scrollbar(request):
    return render(request, 'scrollbar.html', {})

def typography(request):
    return render(request, 'typography.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def search(request):
    return render(request, 'search.html', {})

def blank_page(request):
    return render(request, 'blank-page.html', {})

def error_page(request):
    return render(request, 'error-page.html', {})

def internal_error(request):
    return render(request, 'internal-error.html', {})

def widgets(request):
    return render(request, 'widgets.html', {})

def google_map(request):
    return render(request, 'google-map.html', {})

def notification(request):
    return render(request, 'notification.html', {})

def is_staff_user(user):
    """Check if user is staff"""
    return user.is_authenticated and user.is_staff

@login_required
def lock_screen(request):
    """Lock screen view - user must re-enter password to unlock"""
    error = None
    
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            # Password correct, redirect to dashboard or intended page
            next_url = request.GET.get('next', 'dashboard')
            messages.success(request, 'Screen unlocked successfully!')
            return redirect(next_url)
        else:
            error = 'Password is incorrect. Please try again.'
    
    context = {
        'user': request.user,
        'error': error,
    }
    return render(request, 'lock-screen.html', context)

@user_passes_test(is_staff_user, login_url='login')
def members(request):
    """Members page - only accessible by staff users"""
    search_query = request.GET.get('search', '')
    
    # Get all users with their profiles
    users = User.objects.select_related('profile').all()
    
    # Filter by search query if provided
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(users, 12)  # Show 12 members per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Statistics
    total_users = User.objects.count()
    staff_users = User.objects.filter(is_staff=True).count()
    active_users = User.objects.filter(is_active=True).count()
    users_with_profiles = User.objects.filter(profile__isnull=False).count()
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_users': total_users,
        'staff_users': staff_users,
        'active_users': active_users,
        'users_with_profiles': users_with_profiles,
    }
    return render(request, 'members.html', context)

def account_settings(request):
    return render(request, 'account-settings.html', {})

def change_password(request):
    return render(request, 'change-password.html', {})

def connections(request):
    return render(request, 'connections.html', {})

def privacy_policy(request):
    return render(request, 'privacy-policy.html', {})

def terms_conditions(request):
    return render(request, 'terms-conditions.html', {})
