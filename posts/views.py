from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Flag
from .forms import PostForm, CommentForm, FlagForm
from django.http import HttpResponseForbidden
from django.db import IntegrityError
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator


def post_list_view(request):
    posts = Post.objects.all().order_by('-posted_on')
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/post_list.html', {'page_obj': page_obj})


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


@login_required
def delete_comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('posts:post_detail', pk=comment.post.pk)
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")


@login_required
def toggle_upvote_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user in comment.upvotes.all():
        comment.upvotes.remove(request.user)
    else:
        comment.upvotes.add(request.user)
    return redirect('posts:post_detail', pk=comment.post.pk)


@login_required
def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


@login_required
def flag_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = FlagForm(request.POST)
        if form.is_valid():
            try:
                content_type = ContentType.objects.get_for_model(Post)
                Flag.objects.create(
                    content_type=content_type,
                    object_id=post.id,
                    user=request.user,
                    reason=form.cleaned_data['reason']
                )
                post.is_flagged = True
                post.save()
                messages.success(request, "Post flagged successfully.")
            except IntegrityError:
                messages.error(request, "You have already flagged this post.")
            return redirect('posts:post_detail', pk=post_id)
    else:
        form = FlagForm()
    return render(request, 'posts/flag_post.html', {'form': form, 'post': post})


@login_required
def flag_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = FlagForm(request.POST)
        if form.is_valid():
            try:
                content_type = ContentType.objects.get_for_model(Comment)
                Flag.objects.create(
                    content_type=content_type,
                    object_id=comment.id,
                    user=request.user,
                    reason=form.cleaned_data['reason']
                )
                comment.is_flagged = True
                comment.save()
                messages.success(request, "Comment flagged successfully.")
            except IntegrityError:
                messages.error(
                    request, "You have already flagged this comment.")
            return redirect('posts:post_detail', pk=comment.post.pk)
    else:
        form = FlagForm()
    return render(request, 'posts/flag_comment.html', {'form': form, 'comment': comment})
