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
