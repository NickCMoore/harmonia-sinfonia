from django.test import TestCase, Client
from django.urls import reverse
from .forms import NewsletterForm

class NewsletterTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('newsletter:subscribe')
    
    def test_subscribe_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter:subscribe')
        self.assertIsInstance(response.context['form'], NewsletterForm)
    
    def test_subscribe_view_post_valid(self):
        response = self.client.post(self.url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))
    
    def test_subscribe_view_post_invalid(self):
        response = self.client.post(self.url, {'email': 'invalid-email'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter:subscribe')
        self.assertIsInstance(response.context['form'], NewsletterForm)
