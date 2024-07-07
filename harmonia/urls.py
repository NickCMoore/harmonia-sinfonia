from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('posts/', include('posts.urls')),
    path('events/', include('events.urls')),
    path('profiles/', include('profiles.urls')),
    path('auth/', include('authentication.urls')),
]
