"""
Menu Management Views

Provides views for managing menus through a web interface.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import modelformset_factory
from .models import MenuCategory, MenuItem, MenuSettings, MenuLog
from .forms import MenuCategoryForm, MenuItemForm, MenuSettingsForm, MenuReorderForm


@login_required
@permission_required('menu_management.view_menuitem', raise_exception=True)
def menu_dashboard(request):
    """Menu management dashboard"""
    categories = MenuCategory.objects.annotate(
        item_count=Count('menu_items')
    ).order_by('order')
    
    recent_logs = MenuLog.objects.select_related(
        'user', 'menu_item', 'category'
    )[:10]
    
    stats = {
        'total_categories': categories.count(),
        'total_menus': MenuItem.objects.count(),
        'active_menus': MenuItem.objects.filter(is_active=True).count(),
        'inactive_menus': MenuItem.objects.filter(is_active=False).count(),
    }
    
    context = {
        'categories': categories,
        'recent_logs': recent_logs,
        'stats': stats,
        'title': 'Menu Management Dashboard'
    }
    return render(request, 'menu_management/dashboard.html', context)


class MenuCategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List view for menu categories"""
    model = MenuCategory
    template_name = 'menu_management/category_list.html'
    context_object_name = 'categories'
    permission_required = 'menu_management.view_menucategory'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = MenuCategory.objects.annotate(
            item_count=Count('menu_items')
        ).order_by('order')
        
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(slug__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Menu Categories'
        context['search_query'] = self.request.GET.get('search', '')
        return context


class MenuCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create view for menu categories"""
    model = MenuCategory
    form_class = MenuCategoryForm
    template_name = 'menu_management/category_form.html'
    permission_required = 'menu_management.add_menucategory'
    
    def get_success_url(self):
        return reverse('menu_management:category_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Menu category created successfully.')
        return super().form_valid(form)


class MenuCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update view for menu categories"""
    model = MenuCategory
    form_class = MenuCategoryForm
    template_name = 'menu_management/category_form.html'
    permission_required = 'menu_management.change_menucategory'
    
    def get_success_url(self):
        return reverse('menu_management:category_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Menu category updated successfully.')
        return super().form_valid(form)


class MenuCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete view for menu categories"""
    model = MenuCategory
    template_name = 'menu_management/category_confirm_delete.html'
    permission_required = 'menu_management.delete_menucategory'
    
    def get_success_url(self):
        return reverse('menu_management:category_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Menu category deleted successfully.')
        return super().delete(request, *args, **kwargs)


class MenuItemListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List view for menu items"""
    model = MenuItem
    template_name = 'menu_management/menu_list.html'
    context_object_name = 'menu_items'
    permission_required = 'menu_management.view_menuitem'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = MenuItem.objects.select_related(
            'category', 'parent', 'created_by'
        ).order_by('category__order', 'order', 'title')
        
        # Filter by category
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Filter by parent
        parent_id = self.request.GET.get('parent')
        if parent_id:
            queryset = queryset.filter(parent_id=parent_id)
        elif parent_id == '0':  # Top level items
            queryset = queryset.filter(parent__isnull=True)
        
        # Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(slug__icontains=search) |
                Q(url_name__icontains=search)
            )
        
        # Filter by status
        status = self.request.GET.get('status')
        if status == 'active':
            queryset = queryset.filter(is_active=True)
        elif status == 'inactive':
            queryset = queryset.filter(is_active=False)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Menu Items'
        context['categories'] = MenuCategory.objects.all()
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_status'] = self.request.GET.get('status', '')
        return context


class MenuItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create view for menu items"""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu_management/menu_form.html'
    permission_required = 'menu_management.add_menuitem'
    
    def get_success_url(self):
        return reverse('menu_management:menu_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Menu item created successfully.')
        return super().form_valid(form)


class MenuItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update view for menu items"""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu_management/menu_form.html'
    permission_required = 'menu_management.change_menuitem'
    
    def get_success_url(self):
        return reverse('menu_management:menu_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Menu item updated successfully.')
        return super().form_valid(form)


class MenuItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete view for menu items"""
    model = MenuItem
    template_name = 'menu_management/menu_confirm_delete.html'
    permission_required = 'menu_management.delete_menuitem'
    
    def get_success_url(self):
        return reverse('menu_management:menu_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Menu item deleted successfully.')
        return super().delete(request, *args, **kwargs)


@login_required
@permission_required('menu_management.change_menuitem', raise_exception=True)
def menu_reorder(request):
    """Reorder menu items"""
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        menu_orders = request.POST.getlist('menu_order[]')
        
        if category_id and menu_orders:
            category = get_object_or_404(MenuCategory, id=category_id)
            
            for index, menu_id in enumerate(menu_orders):
                MenuItem.objects.filter(
                    id=menu_id, 
                    category=category
                ).update(order=index + 1)
            
            messages.success(request, 'Menu order updated successfully.')
            return JsonResponse({'success': True})
        
        return JsonResponse({'success': False, 'error': 'Invalid data'})
    
    categories = MenuCategory.objects.prefetch_related(
        'menu_items'
    ).order_by('order')
    
    context = {
        'categories': categories,
        'title': 'Reorder Menus'
    }
    return render(request, 'menu_management/menu_reorder.html', context)


@login_required
@permission_required('menu_management.view_menusettings', raise_exception=True)
def menu_settings(request):
    """Menu settings view"""
    settings = MenuSettings.get_settings()
    
    if request.method == 'POST':
        if not request.user.has_perm('menu_management.change_menusettings'):
            messages.error(request, 'You do not have permission to change settings.')
            return redirect('menu_management:menu_settings')
        
        form = MenuSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.updated_by = request.user
            settings.save()
            messages.success(request, 'Menu settings updated successfully.')
            return redirect('menu_management:menu_settings')
    else:
        form = MenuSettingsForm(instance=settings)
    
    context = {
        'form': form,
        'settings': settings,
        'title': 'Menu Settings'
    }
    return render(request, 'menu_management/settings.html', context)


@login_required
@permission_required('menu_management.view_menulog', raise_exception=True)
def menu_logs(request):
    """Menu change logs view"""
    logs = MenuLog.objects.select_related(
        'user', 'menu_item', 'category'
    ).order_by('-timestamp')
    
    # Filter by action
    action = request.GET.get('action')
    if action:
        logs = logs.filter(action=action)
    
    # Filter by user
    user_id = request.GET.get('user')
    if user_id:
        logs = logs.filter(user_id=user_id)
    
    # Search
    search = request.GET.get('search')
    if search:
        logs = logs.filter(
            Q(description__icontains=search) |
            Q(menu_item__title__icontains=search) |
            Q(category__name__icontains=search)
        )
    
    paginator = Paginator(logs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'logs': page_obj,
        'action_choices': MenuLog.ACTION_TYPES,
        'search_query': search,
        'selected_action': action,
        'title': 'Menu Change Logs'
    }
    return render(request, 'menu_management/logs.html', context)


@require_http_methods(["POST"])
@login_required
@permission_required('menu_management.change_menuitem', raise_exception=True)
def toggle_menu_status(request, menu_id):
    """Toggle menu item active status via AJAX"""
    menu_item = get_object_or_404(MenuItem, id=menu_id)
    menu_item.is_active = not menu_item.is_active
    menu_item.save()
    
    return JsonResponse({
        'success': True,
        'is_active': menu_item.is_active,
        'message': f'Menu item {"activated" if menu_item.is_active else "deactivated"} successfully.'
    })


@login_required
@permission_required('menu_management.view_menuitem', raise_exception=True)
def menu_preview(request):
    """Preview menu structure"""
    categories = MenuCategory.objects.filter(
        is_active=True
    ).prefetch_related(
        'menu_items__children'
    ).order_by('order')
    
    context = {
        'categories': categories,
        'title': 'Menu Preview'
    }
    return render(request, 'menu_management/preview.html', context)
