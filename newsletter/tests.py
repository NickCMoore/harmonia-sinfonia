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
