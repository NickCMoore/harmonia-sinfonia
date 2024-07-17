from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Post(models.Model):
    """Model representing a blog post."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the post."""
        return f'{self.user.username} - {self.title[:20]}'

class Comment(models.Model):
    """Model representing a comment on a blog post."""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    is_flagged = models.BooleanField(default=False)

    def total_upvotes(self):
        """Return the total number of upvotes for the comment."""
        return self.upvotes.count()

    def __str__(self):
        """Return a string representation of the comment."""
        return f'Comment by {self.user.username} on {self.post.title}'

class Flag(models.Model):
    """Model representing a flag for inappropriate content."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('content_type', 'object_id', 'user')
