from celery import shared_task
from celery.utils.log import get_task_logger
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from sisys import settings
from sisys.newsletters_app.models import NewsletterUser, Newsletter

logger = get_task_logger(__name__)


@shared_task
def send_mail_to_all():
    # mail = Newsletter.objects.all().first()
    subscribers = NewsletterUser.objects.all()
    for user in subscribers:
        email_subject = 'welcome to news!'
        email_body = 'this is first news'
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        email.send()
    return redirect('home')
