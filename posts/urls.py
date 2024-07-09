from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts_list/', views.post_list_view, name='post_list'),
    path('posts_detail/<int:pk>/', views.post_detail_view, name='post_detail'),
]
