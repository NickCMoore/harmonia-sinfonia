from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'image', 'total_likes')


admin.site.register(Event, EventAdmin)
