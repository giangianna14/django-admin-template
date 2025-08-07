"""
E-commerce admin configuration.
"""
from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, Review, Seller


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock_quantity', 'is_active')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin."""
    list_display = ('user', 'phone', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    list_filter = ('created_at',)


class OrderItemInline(admin.TabularInline):
    """Order item inline."""
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin."""
    list_display = ('pk', 'customer', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__user__username', 'customer__user__email')
    list_editable = ('status',)
    inlines = [OrderItemInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Review admin."""
    list_display = ('product', 'customer', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'customer__user__username')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    """Seller admin."""
    list_display = ('company_name', 'user', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('company_name', 'user__username')
    list_editable = ('is_verified',)
