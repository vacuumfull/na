"""Admin models for Blog app"""
from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    fields = ['title', 'author', 'image', 'annotation', 'content', 'published']
