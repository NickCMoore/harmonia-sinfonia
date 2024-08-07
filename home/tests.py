from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Notification
from newsletter.models import Subscriber

class HomeTests(TestCase):

    def setUp(self):
        """Set up the test environment with a user, notifications, and a subscriber."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.notification1 = Notification.objects.create(recipient=self.user, message="Your account has been suspended.")
        self.notification2 = Notification.objects.create(recipient=self.user, message="Welcome to the platform!")
        self.subscriber = Subscriber.objects.create(email='subscriber@example.com')

    def test_home_view_authenticated(self):
        """Test the home view for an authenticated user."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.notification1.message)
        self.assertContains(response, self.notification2.message)

    def test_home_view_unauthenticated(self):
        """Test the home view for an unauthenticated user."""
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.notification1.message)
        self.assertNotContains(response, self.notification2.message)

    def test_home_view_post_subscription(self):
        """Test the newsletter subscription via home view."""
        response = self.client.post(reverse('home:home'), {'email': 'newsubscriber@example.com'})
        self.assertRedirects(response, reverse('home:home'))
        self.assertTrue(Subscriber.objects.filter(email='newsubscriber@example.com').exists())

    def test_learn_more_view_authenticated(self):
        """Test the learn more view for an authenticated user."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('home:learn_more'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.notification1.message)
        self.assertContains(response, self.notification2.message)

    def test_learn_more_view_unauthenticated(self):
        """Test the learn more view for an unauthenticated user."""
        response = self.client.get(reverse('home:learn_more'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.notification1.message)
        self.assertNotContains(response, self.notification2.message)
