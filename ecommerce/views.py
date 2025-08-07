"""
E-commerce views for products, orders, customers, etc.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def products_grid(request):
    """Products grid view."""
    return render(request, 'ecommerce/products-grid.html', {})


@login_required
def products_list(request):
    """Products list view."""
    return render(request, 'ecommerce/products-list.html', {})


@login_required
def product_details(request):
    """Product details view."""
    return render(request, 'ecommerce/product-details.html', {})


@login_required
def create_product(request):
    """Create product view."""
    return render(request, 'ecommerce/create-product.html', {})


@login_required
def edit_product(request):
    """Edit product view."""
    return render(request, 'ecommerce/edit-product.html', {})


@login_required
def cart(request):
    """Shopping cart view."""
    return render(request, 'ecommerce/cart.html', {})


@login_required
def checkout(request):
    """Checkout view."""
    return render(request, 'ecommerce/checkout.html', {})


@login_required
def orders(request):
    """Orders list view."""
    return render(request, 'ecommerce/orders.html', {})


@login_required
def order_details(request):
    """Order details view."""
    return render(request, 'ecommerce/order-details.html', {})


@login_required
def create_order(request):
    """Create order view."""
    return render(request, 'ecommerce/create-order.html', {})


@login_required
def order_tracking(request):
    """Order tracking view."""
    return render(request, 'ecommerce/order-tracking.html', {})


@login_required
def customers(request):
    """Customers list view."""
    return render(request, 'ecommerce/customers.html', {})


@login_required
def customer_details(request):
    """Customer details view."""
    return render(request, 'ecommerce/customer-details.html', {})


@login_required
def categories(request):
    """Product categories view."""
    return render(request, 'ecommerce/categories.html', {})


@login_required
def sellers(request):
    """Sellers list view."""
    return render(request, 'ecommerce/sellers.html', {})


@login_required
def seller_details(request):
    """Seller details view."""
    return render(request, 'ecommerce/seller-details.html', {})


@login_required
def create_seller(request):
    """Create seller view."""
    return render(request, 'ecommerce/create-seller.html', {})


@login_required
def reviews(request):
    """Product reviews view."""
    return render(request, 'ecommerce/reviews.html', {})


@login_required
def refunds(request):
    """Refunds view."""
    return render(request, 'ecommerce/refunds.html', {})


@login_required
def customers_two(request):
    """Alternative customers view."""
    return render(request, 'ecommerce/customers-2.html', {})
