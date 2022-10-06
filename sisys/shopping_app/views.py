import asyncio
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from shopping_app.forms import ItemCreationForm
from shopping_app.mixins import required_group
from shopping_app.models import Product, OrderItem, Order, ShippingAddress
from shopping_app.utils import resize_image, get_context_attributes
from django.core.paginator import Paginator

from sisys.utils import send_order_to_staff, send_order_confirmation_mail

loop = asyncio.get_event_loop()


def shop_home(request):
    user = request.user
    products = Product.objects.all()
    products_paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page = products_paginator.get_page(page_number)
    context_data = get_context_attributes(request, user)
    context = {
        'items': products,
        'page': page,
        'products_paginator': products_paginator,
        'user': user,
        'cart_items': context_data['cart_items']
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, pk):
    item = Product.objects.all().get(id=pk)
    user = request.user
    context_data = get_context_attributes(request, user)

    context = {
        'product': item,
        'cart_items': context_data['cart_items'],

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
    user = request.user
    context_data = get_context_attributes(request, user)

    context = {
        'items': context_data['items'],
        'order': context_data['order'],
        'cart_items': context_data['cart_items'],
    }
    return render(request, 'shop/cart.html', context)


@login_required()
def checkout(request):
    user = request.user
    context_data = get_context_attributes(request, user)
    cart_items = context_data['cart_items']
    if cart_items > 0:
        context = {
            'user': user,
            'items': context_data['items'],
            'order': context_data['order'],
            'cart_items': context_data['cart_items'],
        }
        return render(request, 'shop/checkout.html', context)
    else:
        return render(request, 'shop/empty-cart-checkout.html')


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
    email = data['form']['email']
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    mail_data = str(data) + str.join(" ;",
                                     [f'{item.product.name} price: {item.product.price} quantity: {item.quantity}' for
                                      item in
                                      order.orderitem_set.all()])
    if total == order.get_cart_total:
        order.complete = True
        loop.run_in_executor(None, send_order_to_staff, mail_data)
        loop.run_in_executor(None, send_order_confirmation_mail, email)
    order.save()
    if order.shipping is True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            email=data['form']['email'],
            name=data['form']['name'],
            address=data['shipping']['address'],
            province=data['shipping']['province'],
            city=data['shipping']['city'],
            post_code=data['shipping']['postcode'],
            phone=data['shipping']['phone'],

        )
    return JsonResponse('Payment complete.', safe=False)
