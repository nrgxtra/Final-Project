from django.shortcuts import render

from shopping_app.models import Item


def shop_home(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'shop/shop.html', context)
