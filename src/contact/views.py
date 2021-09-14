from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add


def index(request):
    add.delay(5, 6)
    return HttpResponse("<h1>Hello, world</h1>")


def contact_view(request):
    send_mail('sally, this is subject',
              'celery sally, hello world, this is message body',
              '',
              ['oytizzo@gmail.com'],
              fail_silently=False)
    context = {}
    return render(request, 'contact/contact.html', context)
