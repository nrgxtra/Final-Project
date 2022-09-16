from django import forms

from shopping_app.models import Product


class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



