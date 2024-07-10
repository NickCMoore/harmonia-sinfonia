from django.urls import path
from .views import post_list_view, post_detail_view, create_post_view, delete_post_view, toggle_like_view, delete_comment_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', create_post_view, name='create_post'),
    path('post/<int:pk>/delete/', delete_post_view, name='delete_post'),
    path('post/<int:pk>/toggle_like/', toggle_like_view, name='toggle_like'),
    path('comment/<int:pk>/delete/', delete_comment_view, name='delete_comment'),
]
