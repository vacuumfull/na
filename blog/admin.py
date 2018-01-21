"""Admin models for Blog app."""
from django.contrib import admin
# from taggit.managers import TaggableManager

from blog.models import Blog, Comment


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    """Admin panel for Blogs model."""

    fieldsets = (
        ('Заголовок', {'fields': ('title', 'rubric', 'author',
                                  'image', 'annotation')}),
        ('Содержание', {'fields': ('content', 'published', 'tags')}),
        ('Связки', {'fields': ('event', 'place')}),
    )
    list_display = ('title', 'rubric', 'author', 'published', 'created_at')
    list_editable = ('rubric', 'published',)
    list_filter = ('rubric', 'published', 'created_at')
    search_fields = ('title', 'author__username')


@admin.register(Comment)
class AdminBlogComment(admin.ModelAdmin):
    """Admin panel for Blog comment system."""

    list_display = ('blog', 'user', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
