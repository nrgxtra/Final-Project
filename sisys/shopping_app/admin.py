from django.contrib import admin

from shopping_app.models import *

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    list_filter = ('user',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_ordered', 'complete', 'transaction_id')
    list_filter = ('date_ordered',)
