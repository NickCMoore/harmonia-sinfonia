from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def learn_more(request):
    return render(request, 'home/learn_more.html')
