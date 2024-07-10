from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Notification


@login_required
def profile_list_view(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})


@login_required
def profile_detail_view(request, identifier):
    try:
        user_id = int(identifier)
        user = get_object_or_404(User, id=user_id)
    except ValueError:
        user = get_object_or_404(User, username=identifier)

    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    profile = user.profile
    return render(request, 'profiles/profile_detail.html', {'profile': profile})


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
    return redirect('profile_detail', identifier=username)


@login_required
def following_list(request):
    following = request.user.following.all()
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
