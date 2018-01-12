"""Admin models from Teams app"""
from django.contrib import admin

from band.models import Band


@admin.register(Band)
class AdminTeam(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'owner', 'members', 'published', 'tags')
    list_display = ('name', 'published', 'slug')
    # filter_horizontal = ('tags',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title',)
