from django.shortcuts import render


def home_view(request):
    return render(request, 'home/home.html')


def learn_more_view(request):
    return render(request, 'home/learn_more.html')
