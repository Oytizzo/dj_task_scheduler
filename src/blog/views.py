from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    queryset = Post.objects.all()

    return render(request, 'blog/home.html', {'posts': queryset})


class PostListView(ListView):
    # template_name = 'blog/post_list.html'     # default
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    # template_name = 'blog/post_detail.html'   # default
    model = Post
    context_object_name = 'post'
