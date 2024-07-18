from .models import Notification

def unread_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        return {'unread_notifications': notifications}
    return {'unread_notifications': []}
