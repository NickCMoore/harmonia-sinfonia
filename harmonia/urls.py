from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts')),
    path('events/', include('events.urls', namespace='events')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('', include('home.urls', namespace='home')),
]
