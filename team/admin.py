"""Admin models from Teams app"""
from django.contrib import admin

from team.models import Team


@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    fields = ('name', 'logo', 'description', 'member', 'published')
    list_display = ('name', 'published', 'slug')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title',)
