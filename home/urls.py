from django.urls import path
from .views import home, learn_more

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('learn_more/', learn_more, name='learn_more'),
]
