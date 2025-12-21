from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import ShowPage
from .services import get_posts, get_image


# Show all pages
def Posts(request):
    posts = get_posts()
    images = get_image()
    print("images:", images)
    
    ctx = {
        'posts': posts,
        'images': images,
    }
    return render(request, 'show/show_ann.html', ctx)
