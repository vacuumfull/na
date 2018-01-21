"""Admin models for Blog app."""
from django.contrib import admin
# from taggit.managers import TaggableManager

from playlist.models import Playlist


@admin.register(Playlist)
class AdminPlaylist(admin.ModelAdmin):
    """Admin panel for Blogs model."""

    fieldsets = (
        ('Заголовок', {'fields': ('name', 'creator',
                                  'image', 'annotation')}),
        ('Содержание', {'fields': ('content', 'published', 'tags')}),
    )
    list_display = ('name', 'creator', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
    search_fields = ('name', 'creator__username')