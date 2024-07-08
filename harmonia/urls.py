from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('authentication/', include(('authentication.urls',
         'authentication'), namespace='authentication')),
]
