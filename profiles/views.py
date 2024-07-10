from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Notification
from .forms import UserProfileForm


@login_required
def profile_list_view(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})


@login_required
def profile_detail_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profiles/profile_detail.html', {'user_profile': profile})


@login_required
def follow_unfollow(request, username):
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
    following = request.user.profile.followers.all()
    return render(request, 'profiles/following_list.html', {'following': following})


@login_required
def notifications_list(request):
    notifications = request.user.notifications.all()
    return render(request, 'profiles/notifications_list.html', {'notifications': notifications})


@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id, recipient=request.user)
    notification.read = True
    notification.save()
    return redirect('profiles:notifications_list')


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id, recipient=request.user)
    notification.delete()
    return redirect('profiles:notifications_list')


@login_required
def edit_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_detail', username=username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
