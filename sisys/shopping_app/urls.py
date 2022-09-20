from django.urls import path

from shopping_app.views import shop_home, item_details, show_cart, checkout, updateItem, processOrder, delete_item, \
    update_item, create_item

urlpatterns = (
    path('shop', shop_home, name='shop-home'),
    path('add-item', create_item, name='add-item'),
    path('update-item <pk>', update_item, name='update-item'),
    path('delete-item <pk>', delete_item, name='delete-item'),
    path('item-details <pk>', item_details, name='item-details'),
    path('shopping-cart', show_cart, name='shopping-cart'),
    path('checkout', checkout, name='checkout'),
    path('update_item', updateItem, name='update_item'),
    path('process_order', processOrder, name='process_order'),
)
