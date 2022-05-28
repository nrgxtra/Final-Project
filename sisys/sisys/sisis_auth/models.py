from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from sisys.sisis_auth.managers import SisisUserManager


class SisisUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.TimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'
    objects = SisisUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17, blank=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
    )
    user = models.OneToOneField(
        SisisUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
