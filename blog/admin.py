"""Admin models for Blog app."""
from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    """Admin panel for Blogs model."""

    fieldsets = (
        ('Заголовок', {'fields': ('title', 'rubric', 'author',
                                  'image', 'annotation')}),
        ('Содержание', {'fields': ('content', 'published')}),
        ('Связки', {'fields': ('event', 'place')}),
    )
    list_display = ('title', 'rubric', 'author', 'published', 'created_at')
    list_editable = ('rubric', 'published',)
    list_filter = ('rubric', 'published', 'created_at')
    search_fields = ('title', 'author__username')
