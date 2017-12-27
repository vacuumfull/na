"""Admin models from Places app"""
from django.contrib import admin

from event.models import Comment, Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('title', 'owner', 'date', 'price', 'description',
                       'image', 'published')}),
        ('Содержание', {'fields': ('tags','locations', 'bands', 'musicians')}),
    )

    filter_horizontal = ('tags',)
    list_display = ('title', 'price', 'published', 'date')
    list_editable = ('published',)
    list_filter = ('published', 'date', 'price')
    search_fields = ('title',)


@admin.register(Comment)
class AdminBlogComment(admin.ModelAdmin):
    """Admin panel for Blog comment system."""

    list_display = ('event', 'user', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
