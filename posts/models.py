from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
