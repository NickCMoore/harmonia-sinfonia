from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title