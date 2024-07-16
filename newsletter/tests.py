from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Subscriber
from .forms import NewsletterForm

class NewsletterTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('newsletter:subscribe')
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_subscribe_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/subscribe.html')
        self.assertIsInstance(response.context['form'], NewsletterForm)

    def test_subscribe_view_post_valid(self):
        response = self.client.post(self.url, {'email': 'newsubscriber@example.com'})
        self.assertRedirects(response, reverse('home:home'))
        self.assertTrue(Subscriber.objects.filter(email='newsubscriber@example.com').exists())

    def test_subscribe_view_post_invalid(self):
        response = self.client.post(self.url, {'email': 'invalid-email'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/subscribe.html')
        self.assertFalse(Subscriber.objects.filter(email='invalid-email').exists())
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_subscribe_view_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/subscribe.html')
        self.assertIsInstance(response.context['form'], NewsletterForm)