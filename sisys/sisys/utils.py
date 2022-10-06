from django.core.mail import EmailMessage

from sisys import settings


def send_order_to_staff(data):
    email_subject = 'New Order'
    email_body = data
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
    )
    email.send()


def send_order_confirmation_mail(email):
    email_subject = 'We received Your order'
    email_body = f'Once it`s proceeded, we will inform You!\nThank You for beeng part of our exclusive experience!'
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    email.send()
