

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group

from sisis_auth.managers import SisisUserManager


class SisisUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,)
    is_staff = models.BooleanField(default=False,)
    date_joined = models.TimeField(auto_now_add=True,)
    is_active = models.BooleanField(default=False)

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
    phone_regex = RegexValidator(regex=r"^[\+][3][4][0-9]{9}$",
                                 message="Phone number must be entered in the format: '+34000000000'. Exactly 11 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=12, blank=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
    )
    bio = models.TextField(blank=True, null=True)
    fb_link = models.CharField(max_length=300, blank=True, null=True)
    vimeo_link = models.CharField(max_length=300, blank=True, null=True)
    tweeter_link = models.CharField(max_length=300, blank=True, null=True)
    link_link = models.CharField(max_length=300, blank=True, null=True)
    user = models.OneToOneField(
        SisisUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
