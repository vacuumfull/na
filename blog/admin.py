"""Admin models for Blog app"""
from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    fieldsets = (
        ('Заголовок', {'fields': ('title', 'author', 'image', 'annotation')}),
        ('Содержание', {'fields': ('content', 'published')}),
    )
    list_display = ('title', 'author', 'published', 'created_at')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'author__username')
