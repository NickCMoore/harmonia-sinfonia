from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Notification
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def handle_profile_save(sender, instance, **kwargs):
    if instance.is_suspended:
        send_suspension_notification(instance.user, instance.suspension_reason)


def send_suspension_notification(user, reason):
    admin_user = User.objects.filter(is_superuser=True).first()
    message = f'Your account has been suspended. Reason: {reason}'
    Notification.objects.create(
        recipient=user,
        sender=admin_user,
        message=message,
    )
