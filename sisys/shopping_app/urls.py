from django.urls import path

from shopping_app.views import shop_home, create_item, update_item, delete_item, item_details

urlpatterns = (
    path('shop', shop_home, name='shop-home'),
    path('add-item', create_item, name='add-item'),
    path('update-item <pk>', update_item, name='update-item'),
    path('delete-item <pk>', delete_item, name='delete-item'),
    path('item-details <pk>', item_details, name='item-details'),
)
