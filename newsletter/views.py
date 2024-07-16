from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm
from django.core.exceptions import ValidationError

class SubscribeView(View):
    """Handle newsletter subscription views."""

    def get(self, request):
        """Display the subscription form."""
        form = NewsletterForm()
        return render(request, 'newsletter/subscribe.html', {'form': form})

    def post(self, request):
        """Handle the subscription form submission."""
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you for subscribing to our newsletter!')
                return redirect('home:home')
            except ValidationError as e:
                messages.error(request, f"Error during subscription: {e}")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {e}")
        else:
            messages.error(request, "There was an error with your subscription. Please check the details and try again.")
        return render(request, 'newsletter/subscribe.html', {'form': form})
