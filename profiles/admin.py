from django.contrib import admin
from .models import Profile, Notification
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Notification)


def synchronize_profile_ids(modeladmin, request, queryset):
    for user in queryset:
        profiles = Profile.objects.filter(user=user)

        if profiles.exists():
            main_profile = profiles[0]
            for profile in profiles[1:]:
                profile.delete()
            if main_profile.id != user.id:
                Profile.objects.filter(id=user.id).delete()
                main_profile.id = user.id
                main_profile.save()
        else:
            Profile.objects.create(user=user, id=user.id)


synchronize_profile_ids.short_description = "Synchronize Profile IDs with User IDs"


class UserAdmin(admin.ModelAdmin):
    actions = [synchronize_profile_ids]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
