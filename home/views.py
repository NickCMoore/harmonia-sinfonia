from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Notification
from newsletter.forms import NewsletterForm
from django.contrib import messages
from django.core.exceptions import ValidationError

def home_view(request):
    """Display the home page and handle newsletter subscription."""
    user = request.user
    suspension_notification = None
    other_notifications = None

    if user.is_authenticated:
        notifications = user.notifications.all()
        suspension_notification = notifications.filter(message__icontains='suspended').first()
        other_notifications = notifications.exclude(message__icontains='suspended')

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you for subscribing!')
                return redirect('home:home')
            except ValidationError as e:
                messages.error(request, f"Error during subscription: {e}")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {e}")
    else:
        form = NewsletterForm()

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
        'form': form
    }
    return render(request, 'home/home.html', context)

def learn_more_view(request):
    """Display the learn more page."""
    user = request.user
    suspension_notification = None
    other_notifications = None

    if user.is_authenticated:
        notifications = user.notifications.all()
        suspension_notification = notifications.filter(message__icontains='suspended').first()
        other_notifications = notifications.exclude(message__icontains='suspended')

    context = {
        'suspension_notification': suspension_notification,
        'other_notifications': other_notifications,
    }
    return render(request, 'home/learn_more.html', context)
