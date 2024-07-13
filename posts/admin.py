from django.contrib import admin
from .models import Post, Comment


def unflag_posts(modeladmin, request, queryset):
    queryset.update(is_flagged=False)
    modeladmin.message_user(request, "Selected posts have been unflagged.")


unflag_posts.short_description = "Unflag selected posts"


def unflag_comments(modeladmin, request, queryset):
    queryset.update(is_flagged=False)
    modeladmin.message_user(request, "Selected comments have been unflagged.")


unflag_comments.short_description = "Unflag selected comments"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_flagged')
    list_filter = ('is_flagged',)
    actions = [unflag_posts]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post', 'is_flagged')
    list_filter = ('is_flagged',)
    actions = [unflag_comments]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
