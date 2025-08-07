"""
E-commerce URLs configuration.
"""
from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('products/', views.products_grid, name='products'),  # Alias for products-grid
    path('products-grid/', views.products_grid, name='products-grid'),
    path('products-list/', views.products_list, name='products-list'),
    path('product-details/', views.product_details, name='product-details'),
    path('create-product/', views.create_product, name='create-product'),
    path('edit-product/', views.edit_product, name='edit-product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('order-details/', views.order_details, name='order-details'),
    path('create-order/', views.create_order, name='create-order'),
    path('order-tracking/', views.order_tracking, name='order-tracking'),
    path('customers/', views.customers, name='customers'),
    path('customer-details/', views.customer_details, name='customer-details'),
    path('categories/', views.categories, name='categories'),
    path('sellers/', views.sellers, name='sellers'),
    path('seller-details/', views.seller_details, name='seller-details'),
    path('create-seller/', views.create_seller, name='create-seller'),
    path('reviews/', views.reviews, name='reviews'),
    path('refunds/', views.refunds, name='refunds'),
    path('customers-2/', views.customers_two, name='customers-2'),
]
