from django.urls import path
from .views import posts_list

app_name = 'posts'

urlpatterns = [
    path('', posts_list, name='posts_list'),
]
