from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from shopping_app.forms import ItemCreationForm
from shopping_app.models import Item
from shopping_app.utils import resize_image


def shop_home(request):
    user = request.user
    context = {
        'items': Item.objects.all(),
        'user': user,
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, pk):
    item = Item.objects.all().get(id=pk)
    context = {
        'item': item,
    }
    return render(request, 'shop/item-details.html', context)





@login_required
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


@login_required
def update_item(request, pk):
    user = request.user
    item = Item.objects.all().get(id=pk)

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


def delete_item(request, pk):
    user = request.user
    item = Item.objects.all().get(id=pk)
    if request.method == 'POST':
        if user.is_staff:
            item.delete()
            return redirect('shop-home')
    context = {
        'item': item,
        'user': user,
    }
    return render(request, 'shop/item-delete.html', context)
