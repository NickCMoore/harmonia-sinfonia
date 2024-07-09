from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list_view(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
