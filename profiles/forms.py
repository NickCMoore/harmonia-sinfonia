from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'profile_pic', 'bg_pic']
