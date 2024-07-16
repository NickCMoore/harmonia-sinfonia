from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile, Notification
from posts.models import Post
from django.utils import timezone

class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, display_name='Test User')
        self.notification = Notification.objects.create(recipient=self.user, message='Test notification')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.profile2 = Profile.objects.create(user=self.user2, display_name='Test User 2')
        self.post = Post.objects.create(content='Test post content', user=self.user)

