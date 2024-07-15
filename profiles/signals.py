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
def send_suspension_notification(sender, instance, **kwargs):
    if instance.is_suspended:
        message = f'Your account has been suspended. Reason: {instance.suspension_reason}'
        Notification.objects.get_or_create(
            recipient=instance.user,
            sender=None,
            defaults={'message': message}
        )
