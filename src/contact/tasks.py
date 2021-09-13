# Create your tasks here

from celery import shared_task
# from demoapp.models import Widget


@shared_task
def add(x, y):
    return x + y
