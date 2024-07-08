from django.urls import path
from .views import ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('<int:user_id>/', ProfileDetailView.as_view(), name='profile_detail'),
]
