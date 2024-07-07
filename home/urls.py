from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn_more/', views.learn_more, name='learn_more'),
]