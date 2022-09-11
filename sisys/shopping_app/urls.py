from django.urls import path

from shopping_app.views import shop_home, create_item, update_item

urlpatterns = (
    path('shop', shop_home, name='shop-home'),
    path('add-item', create_item, name='add-item'),
    path('update-item <pk>', update_item, name='update-item'),
)
