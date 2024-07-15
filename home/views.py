from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Notification
from newsletter.forms import NewsletterForm
from django.contrib import messages


def home_view(request):
    user = request.user
    if request.user.is_authenticated:
        notifications = user.notifications.all()
        suspension_notification = notifications.filter(
            message__icontains='suspended').first()
        other_notifications = notifications.exclude(
            message__icontains='suspended')
    else:
        suspension_notification = None
        other_notifications = None

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home:home')
    else:
        form = NewsletterForm()

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
        'form': form
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
