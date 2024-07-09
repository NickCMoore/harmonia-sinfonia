from django.urls import path
from .views import post_list_view, post_detail_view, create_post_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', create_post_view, name='create_post'),
]
