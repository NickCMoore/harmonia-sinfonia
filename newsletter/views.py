from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm


class SubscribeView(View):
    def get(self, request):
        form = NewsletterForm()
        return render(request, 'newsletter/subscribe.html', {'form': form})

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you for subscribing to our newsletter!')
            return redirect('home:home')
        return render(request, 'newsletter/subscribe.html', {'form': form})
