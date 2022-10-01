from django.forms import forms


class BookingForm(forms.Form):
    field_order = ('name', 'email', 'phone number', 'message',)

