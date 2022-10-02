from django.conf import settings
from django.core.mail import EmailMessage


def send_appointment_confirmation_mail(email):
    email_subject = 'We received your booking request'
    email_body = 'Our costumer support will contact You to clarify details.'
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    email.send()


def send_appointment_to_staff(form):
    email_subject = 'New Booking Request'
    email_body = form
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
    )
    email.send()
