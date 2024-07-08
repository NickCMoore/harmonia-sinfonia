from django.urls import path
from .views import EventDetailView, EventListView

app_name = 'events'

urlpatterns = [
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('', EventListView.as_view(), name='event_list'),
]
