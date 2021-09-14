from django.core.mail import send_mail

from celery import shared_task
# from demoapp.models import Widget


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_mail_task():
    send_mail('celery python this is subject',
              'sally, hello world, this is message body',
              '',
              ['oytizzo@gmail.com'],
              fail_silently=False)


@shared_task
def send_email_task(subject, message, sender, cc_myself):
    message_to_email = message + f"\n\nEmailed From: {sender}"

    recipients = ['oytizzo@gmail.com']
    if cc_myself:
        recipients.append(sender)
    send_mail(subject, message_to_email, sender, recipients, fail_silently=False)
