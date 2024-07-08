from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})


def profile_list_view(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})
