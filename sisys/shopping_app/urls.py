from django.urls import path

from shopping_app.views import shop_home

urlpatterns = (
    path('shop', shop_home, name='shop-home'),
)
