from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'postingan/index.html', {'posts': posts})
