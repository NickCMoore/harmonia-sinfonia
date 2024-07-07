from django.shortcuts import render


def profile_list(request):
    return render(request, 'profiles/profile_list.html')
