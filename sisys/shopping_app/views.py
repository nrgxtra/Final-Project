import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from shopping_app.forms import ItemCreationForm
from shopping_app.models import Product, OrderItem, Order, Customer
from shopping_app.utils import resize_image


def shop_home(request):
    user = request.user
    # order= Order.objects.get(customer=request.user.customer, complete=False)
    context = {
        'items': Product.objects.all(),
        'user': user,
        # 'order': order,
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, pk):
    item = Product.objects.all().get(id=pk)

    context = {
        'product': item,

    }
    return render(request, 'shop/item-details.html', context)


# @login_required
# def create_item(request):
#     user = request.user
#     if request.method == 'POST':
#         if user.is_staff:
#             form = ItemCreationForm(request.POST, request.FILES)
#             if form.is_valid():
#                 item = form.save(commit=False)
#                 if item.picture:
#                     img = resize_image(
#                         item.picture,
#                     )
#                     img.save(item.picture.path)
#                 item.save()
#                 return redirect('shop-home')
#     form = ItemCreationForm()
#     context = {
#         'form': form,
#         'user': request.user,
#     }
#     return render(request, 'shop/item-add.html', context)
#
#
# @login_required
# def update_item(request, pk):
#     user = request.user
#     item = Product.objects.all().get(id=pk)
#
#     if request.method == 'POST':
#         form = ItemCreationForm(request.POST, request.FILES, instance=item)
#         if user.is_staff:
#             if form.is_valid():
#                 item = form.save(commit=False)
#                 if item.picture:
#                     img = resize_image(
#                         item.picture,
#                     )
#                     img.save(item.picture.path)
#                 item.save()
#                 return redirect('shop-home')
#     form = ItemCreationForm(instance=item)
#     context = {
#         'form': form,
#         'user': request.user,
#         'item': item,
#     }
#     return render(request, 'shop/item-update.html', context)
#
#
# def delete_item(request, pk):
#     user = request.user
#     item = Product.objects.all().get(id=pk)
#     if request.method == 'POST':
#         if user.is_staff:
#             item.delete()
#             return redirect('shop-home')
#     context = {
#         'item': item,
#         'user': user,
#     }
#     return render(request, 'shop/item-delete.html', context)


def show_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}

    context = {
        'user': request.user,
        'items': items,
        'order': order,
    }
    return render(request, 'shop/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added.', safe=False)

