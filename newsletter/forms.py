from django import forms
from .models import Subscriber

class NewsletterForm(forms.ModelForm):
    """Form for subscribing to the newsletter."""
    
    class Meta:
        """Meta options for the NewsletterForm."""
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
        }
