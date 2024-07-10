from django.contrib import admin
from .models import Profile, Notification
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Notification)


def synchronize_profile_ids(modeladmin, request, queryset):
    for user in queryset:
        try:
            profile = user.profile
            if profile.id != user.id:
                profile.id = user.id
                profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=user, id=user.id)


synchronize_profile_ids.short_description = "Synchronize Profile IDs with User IDs"


class UserAdmin(admin.ModelAdmin):
    actions = [synchronize_profile_ids]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
