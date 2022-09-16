from django.shortcuts import render, get_object_or_404
from .models import Newsletter

def post_list(request):
    posts = Newsletter.published.all()
    return render(request, 'myapp/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Newsletter, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'myapp/post/detail.html', {'post': post})
# Create your views here.
