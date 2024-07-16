from django.db import models

class Subscriber(models.Model):
    """Model representing a newsletter subscriber."""
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the subscriber's email as its string representation."""
        return self.email
