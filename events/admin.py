from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'image', 'total_likes')

    def total_likes(self, obj):
        return obj.total_likes()

admin.site.register(Event, EventAdmin)
