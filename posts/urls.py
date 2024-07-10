from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/create/', views.create_post_view, name='create_post'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
    path('post/<int:pk>/toggle_like/',
         views.toggle_like_view, name='toggle_like'),
    path('comment/<int:pk>/delete/',
         views.delete_comment_view, name='delete_comment'),
    path('comment/<int:pk>/toggle_upvote/',
         views.toggle_upvote_comment, name='toggle_upvote_comment'),
    path('post/<int:pk>/edit/', views.edit_post_view, name='edit_post'),
]
