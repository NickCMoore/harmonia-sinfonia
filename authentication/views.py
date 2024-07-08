from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:home")
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:home")
    else:
        form = UserCreationForm()
    return render(request, "authentication/signup.html", {"form": form})
