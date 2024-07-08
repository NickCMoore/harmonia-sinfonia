from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('event_list/', views.event_list_view, name='event_list'),
    path('event_detail/<int:pk>/', views.event_detail_view, name='event_detail'),
]
