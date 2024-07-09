from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles/images/')
    bg_pic = models.ImageField(
        upload_to='profiles/bg_images/', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following')
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.display_name[:50]) + '-' + get_random_string(6)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
