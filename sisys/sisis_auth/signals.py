from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from shopping_app.models import Customer
from sisis_auth.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        customer = Customer(user=instance)
        customer.save()

