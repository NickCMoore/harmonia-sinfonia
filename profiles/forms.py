from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'profile_pic', 'bg_pic']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search')
    filter_by = forms.ChoiceField(
        choices=[('posts', 'Posts'), ('users', 'Users')], required=False)
