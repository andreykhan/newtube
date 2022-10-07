from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)


def profile(request):
    context = {
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request):
    context = {
    }
    return render(request, 'posts/post_detail.html', context)
