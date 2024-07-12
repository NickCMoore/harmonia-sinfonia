from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('learn-more/', views.learn_more_view, name='learn_more'),
]
