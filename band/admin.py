"""Admin models from Teams app"""
from django.contrib import admin

from band.models import Band, Comment


@admin.register(Band)
class AdminTeam(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'owner', 'members', 'published', 'tags')
    list_display = ('name', 'published', 'slug')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title',)


@admin.register(Comment)
class AdminTeamComment(admin.ModelAdmin):
    """Admin panel for Blog comment system."""

    list_display = ('band', 'user', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')