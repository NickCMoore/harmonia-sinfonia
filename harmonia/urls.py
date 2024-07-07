from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('posts/', include('posts.urls')),
    path('events/', include('events.urls')),
    path('profile/', include('profiles.urls')),
    path('learn-more/', views.learn_more, name='learn_more'),
]
