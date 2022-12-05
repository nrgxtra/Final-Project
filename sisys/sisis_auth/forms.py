from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from sisis_auth.models import Profile

UserModel = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(),
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password', }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', }))

    class Meta:
        model = UserModel
        fields = (
            'email', 'password1', 'password2',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your address'}),
        }


class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email',)
