from .models import Notification

def send_suspension_notification(user, reason):
    """Send a suspension notification to a user."""
    message = f'Your account has been suspended. Reason: {reason}'
    Notification.objects.create(
        recipient=user,
        sender=None,
        message=message,
    )
