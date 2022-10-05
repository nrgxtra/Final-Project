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
    email_subject = 'We received your booking request'
    email_body = 'Our costumer support will contact You to clarify details.'
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    email.send()
