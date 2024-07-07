from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image')
    bg_pic = CloudinaryField('image', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return self.user.username
