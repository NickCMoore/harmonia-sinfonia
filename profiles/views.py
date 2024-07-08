from django.views.generic import DetailView, ListView
from .models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(user_id=self.kwargs['user_id'])


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
