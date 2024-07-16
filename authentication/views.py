from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.core.exceptions import ValidationError

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:
                user = form.get_user()
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home:home")
            except ValidationError as e:
                messages.error(request, f"Error during login: {e}")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, "authentication/login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully! Welcome!")
                return redirect("posts:post_list")
            except ValidationError as e:
                messages.error(request, f"Error during signup: {e}")
        else:
            messages.error(request, "There was an error with your signup. Please check the details and try again.")
    else:
        form = UserCreationForm()
    return render(request, "authentication/signup.html", {"form": form})

def logout_view(request):
    try:
        logout(request)
        messages.success(request, "Successfully logged out!")
    except Exception as e:
        messages.error(request, f"Error during logout: {e}")
    return redirect('home:home')
