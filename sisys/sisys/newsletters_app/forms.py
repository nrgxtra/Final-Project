from django import forms

from sisys.newsletters_app.models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        exclude = ('time_added',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'}),
            'errors': forms.TextInput(attrs={'class': 'form-control', }),
        }
