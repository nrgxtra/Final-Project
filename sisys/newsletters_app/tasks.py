from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

import sisys.settings
from sisys import settings
from newsletters_app.models import NewsletterUser, Newsletter

logger = get_task_logger(__name__)


@shared_task
def send_async_mail(subject: str, text_msg: str, emails: list, ):
    send_mail(
        subject=subject,
        message=text_msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
    )

    return 'email sent'


@shared_task
def send_scheduled_mails():
    print("sending mail...")
    mail = Newsletter.objects.all().first()
    subscribers = NewsletterUser.objects.only('email')
    subject = mail.title
    message = mail.content
    email_from = settings.EMAIL_HOST_USER
    recipient_list = subscribers
    send_mail(subject, message, email_from, recipient_list, )
    return 'sending newsletter...'
