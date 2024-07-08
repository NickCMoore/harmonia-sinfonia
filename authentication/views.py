from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView, CreateView


class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home:home.html')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class SignupView(CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home:home.html')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response
