from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from newsletters_app.models import NewsletterUser
from newsletters_app.tasks import send_async_mail


@receiver(post_save, sender=NewsletterUser)
def send_confirmation_mail(sender, instance, created, **kwargs):
    if created:
        message = render_to_string(
            'newsletter/subscriber-welcome.html',
            {
                'email': instance.email,
            }
        )
        send_async_mail.delay(
            subject=f"Thank You for subscribing!",
            text_msg='Thanks for joining!',
            emails=[instance.email, ],

        )
