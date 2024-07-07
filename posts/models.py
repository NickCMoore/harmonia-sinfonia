from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image')
    bg_pic = CloudinaryField('image', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='followers')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
