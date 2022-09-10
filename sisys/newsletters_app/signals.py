from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from newsletters_app.models import NewsletterUser
from newsletters_app.tasks import send_async_mail


@receiver(post_save, sender=NewsletterUser)
def send_confirmation_mail(sender, instance, created, **kwargs):
    if created:
        send_async_mail.delay(
            subject=f'Thank You for subscribing!',
            text_msg=f'Thanks for joining! \n You can always unsubscribe from Your account.',
            emails=[instance.email, ],

        )
