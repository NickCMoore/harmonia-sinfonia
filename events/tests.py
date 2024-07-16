from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Event

class EventTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.event = Event.objects.create(title='Test Event', date='2024-12-31', time='12:00:00')

    def test_event_detail_view(self):
        response = self.client.get(reverse('events:event_detail', args=[self.event.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_event_list_view(self):
        response = self.client.get(reverse('events:event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_like_event(self):
        self.client.login(username='testuser', password='password')
        
        response = self.client.post(reverse('events:like_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(self.user in self.event.liked_by.all())

        response = self.client.post(reverse('events:like_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.user in self.event.liked_by.all())

    def test_like_event_requires_login(self):
        response = self.client.post(reverse('events:like_event', args=[self.event.id]))
        self.assertNotEqual(response.status_code, 200)
        self.assertFalse(self.user in self.event.liked_by.all())

