from django import forms

from shopping_app.models import Product, ShippingAddress


class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('name', 'address', 'province', 'city', 'post_code', 'phone', 'email',)
