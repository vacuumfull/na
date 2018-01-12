"""Admin models from Places app"""
from django.contrib import admin

from place.models import Comment, Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    fields = ('title', 'image', 'icon', 'description', 'owner', 'published', 'tags',
              'musicians')
    list_display = ('title', 'published')
    filter_horizontal = ('tags',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'address')


@admin.register(Comment)
class AdminBlogComment(admin.ModelAdmin):
    """Admin panel for Place comment system."""

    list_display = ('place', 'user', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
