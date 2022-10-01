import json
import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from shopping_app.forms import ItemCreationForm
from shopping_app.mixins import required_group
from shopping_app.models import Product, OrderItem, Order, ShippingAddress
from shopping_app.utils import resize_image
from django.core.paginator import Paginator, Page


def shop_home(request):
    user = request.user
    products = Product.objects.all()
    products_paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page = products_paginator.get_page(page_number)
    if user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_quantity
    else:
        order = {'get_cart_total': 0, 'get_cart_quantity': 0, 'shipping': False}
        cart_items = order['get_cart_quantity']

    context = {
        'items': products,
        'page': page,
        'products_paginator': products_paginator,
        'user': user,
        'cart_items': cart_items
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, pk):
    item = Product.objects.all().get(id=pk)
    user = request.user
    if user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_quantity
    else:
        order = {'get_cart_total': 0, 'get_cart_quantity': 0, 'shipping': False}
        cart_items = order['get_cart_quantity']

    context = {
        'product': item,
        'cart_items': cart_items,

    }
    return render(request, 'shop/item-details.html', context)


@required_group(groups=['store managers'])
def create_item(request):
    user = request.user
    if request.method == 'POST':
        if user.is_staff:
            form = ItemCreationForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                if item.picture:
                    img = resize_image(
                        item.picture,
                    )
                    img.save(item.picture.path)
                item.save()
                return redirect('shop-home')
    form = ItemCreationForm()
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'shop/item-add.html', context)


@required_group(groups=['store managers'])
def update_item(request, pk):
    user = request.user
    item = Product.objects.all().get(id=pk)

    if request.method == 'POST':
        form = ItemCreationForm(request.POST, request.FILES, instance=item)
        if user.is_staff:
            if form.is_valid():
                item = form.save(commit=False)
                if item.picture:
                    img = resize_image(
                        item.picture,
                    )
                    img.save(item.picture.path)
                item.save()
                return redirect('shop-home')
    form = ItemCreationForm(instance=item)
    context = {
        'form': form,
        'user': request.user,
        'item': item,
    }
    return render(request, 'shop/item-update.html', context)


@required_group(groups=['store managers'])
def delete_item(request, pk):
    user = request.user
    item = Product.objects.all().get(id=pk)
    if request.method == 'POST':
        if user.is_staff:
            item.delete()
            return redirect('shop-home')
    context = {
        'item': item,
        'user': user,
    }
    return render(request, 'shop/item-delete.html', context)


def show_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0, 'shipping': False}
        cart_items = order['get_cart_quantity']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0, 'shipping': False}
        cart_items = order['get_cart_quantity']

    context = {
        'user': request.user,
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'shop/checkout.html', context)


def updateItemQuantity(request):
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


@login_required
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()
    if order.shipping is True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            email=request.user.email,
            name=data['form']['name'],
            address=data['shipping']['address'],
            province=data['shipping']['province'],
            city=data['shipping']['city'],
            post_code=data['shipping']['postcode'],
            phone=data['shipping']['phone'],

        )
    return JsonResponse('Payment complete.', safe=False)
