from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add, send_mail_task


def index(request):
    add.delay(5, 6)
    return HttpResponse("<h1>Hello, world</h1>")


def contact_view(request):
    send_mail_task.delay()
    context = {}
    return render(request, 'contact/contact.html', context)
