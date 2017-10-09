"""Admin models from Places app"""
from django.contrib import admin

from event.models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    fields = ('title', 'date', 'price', 'description', 'image', 'published')
    list_display = ('title', 'price', 'published', 'date')
    list_editable = ('published',)
    list_filter = ('published', 'date', 'price')
    search_fields = ('title',)
