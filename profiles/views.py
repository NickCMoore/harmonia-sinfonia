from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Notification
from posts.models import Post
from .forms import UserProfileForm, SearchForm

def is_admin(user):
    """Check if the user is an admin."""
    return user.is_staff

@login_required
def profile_list_view(request):
    """Display a list of user profiles."""
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

@login_required
def profile_detail_view(request, username):
    """Display the details of a specific user profile."""
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profiles/profile_detail.html', {'user_profile': profile})

@login_required
def follow_unfollow(request, username):
    """Toggle following and unfollowing a user."""
    target_user = get_object_or_404(User, username=username)
    profile = target_user.profile

    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        message = 'You have unfollowed this user.'
    else:
        profile.followers.add(request.user)
        Notification.objects.create(
            recipient=target_user,
            sender=request.user,
            message=f'{request.user.username} started following you.'
        )
        message = 'You are now following this user.'

    messages.success(request, message)
    return redirect('profiles:profile_detail', username=username)

@login_required
def following_list(request):
    """Display the list of users the current user is following."""
    following = request.user.profile.followers.all()
    return render(request, 'profiles/following_list.html', {'following': following})

@login_required
def notifications_list(request):
    """Display the list of notifications for the current user."""
    notifications = request.user.notifications.all()
    return render(request, 'profiles/notifications_list.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    """Mark a notification as read."""
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.read = True
    notification.save()
    return redirect('profiles:notifications_list')

@login_required
def delete_notification(request, notification_id):
    """Delete a notification."""
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.delete()
    return redirect('profiles:notifications_list')

@login_required
def edit_profile(request, username):
    """Edit a user profile."""
    user_profile = get_object_or_404(Profile, user__username=username)

    if request.user == user_profile.user or request.user.is_staff:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profiles:profile_detail', username=username)
        else:
            form = UserProfileForm(instance=user_profile)
        return render(request, 'profiles/edit_profile.html', {'form': form})
    else:
        messages.error(request, "You do not have permission to edit this profile.")
        return redirect('profiles:profile_detail', username=username)

def search_view(request):
    """Search for users or posts."""
    form = SearchForm(request.GET or None)
    query = None
    filter_by = None
    user_results = []
    post_results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        filter_by = form.cleaned_data.get('filter_by')

        if filter_by == 'users' or not filter_by:
            user_results = Profile.objects.filter(user__username__icontains=query)
        if filter_by == 'posts' or not filter_by:
            post_results = Post.objects.filter(content__icontains=query)

    context = {
        'form': form,
        'query': query,
        'filter_by': filter_by,
        'user_results': user_results,
        'post_results': post_results,
    }
    return render(request, 'profiles/search_results.html', context)
