from django.contrib import admin
from .models import Profile, Notification
from django.contrib.auth.models import User
from .utils import send_suspension_notification

admin.site.register(Notification)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name',
                    'is_suspended_display', 'suspension_reason')
    actions = ['suspend_user', 'unsuspend_user']

    def is_suspended_display(self, obj):
        return obj.is_suspended
    is_suspended_display.boolean = True
    is_suspended_display.short_description = 'Is Suspended'

    def suspend_user(self, request, queryset):
        for profile in queryset:
            profile.is_suspended = True
            profile.suspension_reason = request.POST.get(
                'suspension_reason', 'No reason provided')
            profile.save()
            send_suspension_notification(
                profile.user, profile.suspension_reason)
        self.message_user(request, "Selected users have been suspended.")

    def unsuspend_user(self, request, queryset):
        queryset.update(is_suspended=False, suspension_reason='')
        self.message_user(request, "Selected users have been unsuspended.")

    suspend_user.short_description = "Suspend selected users"
    unsuspend_user.short_description = "Unsuspend selected users"


admin.site.register(Profile, ProfileAdmin)


def synchronize_profile_ids(modeladmin, request, queryset):
    for user in queryset:
        profile, created = Profile.objects.get_or_create(user=user)

        if not created and profile.id != user.id:
            Profile.objects.filter(id=user.id).delete()
            profile.id = user.id
            profile.save()


synchronize_profile_ids.short_description = "Synchronize Profile IDs with User IDs"


class UserAdmin(admin.ModelAdmin):
    actions = [synchronize_profile_ids]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
