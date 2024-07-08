from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='events/images/', blank=True, null=True)

    def __str__(self):
        return self.title
