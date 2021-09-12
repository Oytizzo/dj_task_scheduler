from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    queryset = Post.objects.all()

    return render(request, 'blog/home.html', {'posts': queryset})
