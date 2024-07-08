from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('events/', include('events.urls')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('authentication/', include('authentication.urls')),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
