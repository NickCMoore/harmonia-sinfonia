from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('authentication/', include('authentication.urls')),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
