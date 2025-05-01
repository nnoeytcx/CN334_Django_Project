from django.contrib import admin
from .models import Customer
from .models import Payment
from .models import Shipping
from .models import Product
from .models import Order
from .models import ProductOrder
from .models import Wishlist

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    list_filter = ('province',)
    ordering = ('id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','payment_owner', 'method', 'card_no', 'expired', 'holder_name')
    ordering = ('id',)


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'fee')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category', 'details')
    ordering = ('id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'status', 'customer', 'shipping', 'payment')
    ordering = ('id',)


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'order', 'total_price', 'quantity')
    ordering = ('id',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'user_id')
    ordering = ('id',)

