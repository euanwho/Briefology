from django.shortcuts import render
from django.urls import reverse 
from .models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def index(request):
    return render(request, 'index.html')

def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', {'post':post})
