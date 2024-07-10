from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile_list/', views.profile_list_view, name='profile_list'),
    path('profile_detail/<str:identifier>/',
         views.profile_detail_view, name='profile_detail'),
    path('follow/<str:username>/', views.follow_unfollow, name='follow_unfollow'),
    path('following/', views.following_list, name='following_list'),
    path('notifications/', views.notifications_list, name='notifications_list'),
    path('notifications/mark_as_read/<int:notification_id>/',
         views.mark_notification_as_read, name='mark_notification_as_read'),
    path('notifications/delete/<int:notification_id>/',
         views.delete_notification, name='delete_notification'),
]
