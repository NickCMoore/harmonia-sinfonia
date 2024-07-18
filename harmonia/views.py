from django.shortcuts import render

def home(request):
    """Render the home page."""
    return render(request, 'home.html')

def learn_more(request):
    """Render the learn more page."""
    return render(request, 'learn_more.html')
