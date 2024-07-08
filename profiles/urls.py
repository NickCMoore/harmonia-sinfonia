from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile_list/', views.profile_list_view, name='profile_list'),
    path('profile_detail/<int:pk>/',
         views.profile_detail_view, name='profile_detail'),
]
