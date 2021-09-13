from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add


def index(request):
    add.delay(5, 6)
    return HttpResponse("<h1>Hello, world</h1>")
