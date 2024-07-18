from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    """Admin configuration for the Event model."""
    list_display = ('title', 'date', 'time', 'image', 'total_likes')

    def total_likes(self, obj):
        """Return the total number of likes for the event."""
        return obj.total_likes()

admin.site.register(Event, EventAdmin)
