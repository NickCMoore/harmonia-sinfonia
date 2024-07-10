from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list_view(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment was added!')
            return redirect('posts:post_detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
    else:
        messages.error(request, 'You are not authorized to delete this post.')
    return redirect('posts:post_list')


@login_required
def toggle_like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.success(request, 'You unliked the post.')
    else:
        post.likes.add(request.user)
        messages.success(request, 'You liked the post.')
    return redirect('posts:post_detail', pk=pk)
