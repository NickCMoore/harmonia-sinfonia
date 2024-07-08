from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('authentication/', include(('authentication.urls',
         'authentication'), namespace='authentication')),
    path('newsletter/', include(('newsletter.urls',
         'newsletter'), namespace='newsletter')),
]

# Static and media files handling
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
