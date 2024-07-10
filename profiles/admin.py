from django.contrib import admin
from .models import Profile, Notification
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Notification)


def synchronize_profile_ids(modeladmin, request, queryset):
    for user in queryset:
        profile, created = Profile.objects.get_or_create(
            user=user, defaults={'id': user.id})

        if not created and profile.id != user.id:
            Profile.objects.filter(id=user.id).delete()
            profile.id = user.id
            profile.save()


synchronize_profile_ids.short_description = "Synchronize Profile IDs with User IDs"


class UserAdmin(admin.ModelAdmin):
    actions = [synchronize_profile_ids]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
