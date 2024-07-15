from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import Notification


@login_required
def home_view(request):
    user = request.user
    notifications = user.notifications.all()
    suspension_notification = notifications.filter(
        message__icontains='suspended').first()
    other_notifications = notifications.exclude(message__icontains='suspended')

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
    }
    return render(request, 'home/home.html', context)


@login_required
def learn_more_view(request):
    user = request.user
    notifications = user.notifications.all()
    suspension_notification = notifications.filter(
        message__icontains='suspended').first()
    other_notifications = notifications.exclude(message__icontains='suspended')

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
    }
    return render(request, 'home/learn_more.html', context)
