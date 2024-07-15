from django.shortcuts import render
from profiles.models import Notification


def home_view(request):
    user = request.user
    suspension_notification = None
    other_notifications = None

    if user.is_authenticated:
        notifications = user.notifications.all()
        suspension_notification = notifications.filter(
            message__icontains='suspended').first()
        other_notifications = notifications.exclude(
            message__icontains='suspended')

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
    }
    return render(request, 'home/home.html', context)


def learn_more_view(request):
    user = request.user
    suspension_notification = None
    other_notifications = None

    if user.is_authenticated:
        notifications = user.notifications.all()
        suspension_notification = notifications.filter(
            message__icontains='suspended').first()
        other_notifications = notifications.exclude(
            message__icontains='suspended')

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
    }
    return render(request, 'home/learn_more.html', context)
