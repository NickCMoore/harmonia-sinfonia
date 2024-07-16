from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile, Notification

class ProfileTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password')
        self.profile1, created = Profile.objects.get_or_create(user=self.user1, defaults={'display_name': 'Test User 1'})

        self.user2 = User.objects.create_user(username='testuser2', password='password')
        self.profile2, created = Profile.objects.get_or_create(user=self.user2, defaults={'display_name': 'Test User 2'})

        self.client.login(username='testuser1', password='password')

    def test_profile_list_view(self):
        response = self.client.get(reverse('profiles:profile_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile_list.html')

    def test_profile_detail_view(self):
        response = self.client.get(reverse('profiles:profile_detail', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile_detail.html')

    def test_follow_unfollow(self):
        response = self.client.post(reverse('profiles:follow_unfollow', args=[self.user2.username]))
        self.assertEqual(response.status_code, 302)

    def test_following_list(self):
        response = self.client.get(reverse('profiles:following_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/following_list.html')

    def test_notifications_list(self):
        response = self.client.get(reverse('profiles:notifications_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/notifications_list.html')

    def test_mark_notification_as_read(self):
        notification = Notification.objects.create(recipient=self.user1, sender=self.user2, message='Test Notification')
        response = self.client.post(reverse('profiles:mark_notification_as_read', args=[notification.id]))
        self.assertEqual(response.status_code, 302)  

    def test_delete_notification(self):
        notification = Notification.objects.create(recipient=self.user1, sender=self.user2, message='Test Notification')
        response = self.client.post(reverse('profiles:delete_notification', args=[notification.id]))
        self.assertEqual(response.status_code, 302) 

    def test_edit_profile(self):
        response = self.client.get(reverse('profiles:edit_profile', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')

    def test_search_view(self):
        response = self.client.get(reverse('profiles:search'), {'query': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_results.html')
