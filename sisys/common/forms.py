from django import forms

from common.models import Appointment, Question
from common.widgets import DatePickerInput


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your name'})
        self.fields['date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        self.fields['email'].widget.attrs.update({'placeholder': 'abcd@example.com'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '+34123456789'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your message here'})

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(),
        }


class ContactForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Phone Number'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Your Subject'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your Message'})

    class Meta:
        model = Question
        fields = '__all__'


