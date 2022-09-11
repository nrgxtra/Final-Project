from django import forms

from shopping_app.models import Item


class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



