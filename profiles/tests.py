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

    def test_profile_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profiles:profile_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile_list.html')
        self.assertContains(response, self.profile.display_name)

    def test_profile_detail_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profiles:profile_detail', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile_detail.html')
        self.assertContains(response, self.profile.display_name)

    def test_follow_unfollow(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('profiles:follow_unfollow', args=[self.user2.username]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user in self.profile2.followers.all())

        response = self.client.post(reverse('profiles:follow_unfollow', args=[self.user2.username]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.user in self.profile2.followers.all())

    def test_following_list(self):
        self.client.login(username='testuser', password='12345')
        self.profile2.followers.add(self.user)
        response = self.client.get(reverse('profiles:following_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/following_list.html')
        self.assertContains(response, self.profile2.display_name)

    def test_notifications_list(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profiles:notifications_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/notifications_list.html')
        self.assertContains(response, self.notification.message)

