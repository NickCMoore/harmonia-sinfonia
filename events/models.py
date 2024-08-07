from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    """Model representing an event."""
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_events', blank=True)
    time = models.TimeField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        """Return the event title as its string representation."""
        return str(self.title) if self.title else 'Untitled Event'

    def total_likes(self):
        """Return the total number of likes for the event."""
        return self.liked_by.count()
