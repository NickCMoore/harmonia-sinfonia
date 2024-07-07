from django.urls import path
from .views import profile_list

app_name = 'profiles'

urlpatterns = [
    path('', profile_list, name='profile_list'),
]
