from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    queryset = Post.objects.all()

    return render(request, 'blog/home.html', {'posts': queryset})


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PostListView(ListView):
    # template_name = 'blog/post_list.html'     # default
    model = Post
    context_object_name = 'posts'


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PostDetailView(DetailView):
    # template_name = 'blog/post_detail.html'   # default
    model = Post
    context_object_name = 'post'
