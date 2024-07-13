from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post, Comment, Flag
from .forms import PostForm, CommentForm, FlagForm
from django.http import HttpResponseForbidden


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
    return render(request, 'posts/edit_post.html', {'form': form})


@login_required
def flag_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = FlagForm(request.POST)
        if form.is_valid():
            Flag.objects.create(post=post, user=request.user,
                                reason=form.cleaned_data['reason'])
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
            flag = Flag.objects.create(
                post=comment.post,
                user=request.user,
                reason=form.cleaned_data['reason']
            )
            flag.save()
            messages.success(request, "Comment flagged successfully.")
            return redirect('posts:post_detail', pk=comment.post.pk)
        else:
            messages.error(request, "Please provide a reason for flagging.")
    else:
        form = FlagForm()
    return render(request, 'posts/flag_comment.html', {'form': form, 'comment': comment})


@user_passes_test(lambda u: u.is_staff)
def flagged_content_review(request):
    flagged_posts = Post.objects.filter(is_flagged=True)
    flagged_comments = Comment.objects.filter(is_flagged=True)
    context = {
        'flagged_posts': flagged_posts,
        'flagged_comments': flagged_comments,
    }
    return render(request, 'posts/flagged_content_review.html', context)


@user_passes_test(lambda u: u.is_staff)
def unflag_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.is_flagged = False
    post.save()
    messages.success(request, 'The post has been unflagged.')
    return redirect('flagged_content_review')


@user_passes_test(lambda u: u.is_staff)
def unflag_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_flagged = False
    comment.save()
    messages.success(request, 'The comment has been unflagged.')
    return redirect('flagged_content_review')
