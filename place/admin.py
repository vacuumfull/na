"""Admin models from Places app"""
from django.contrib import admin

from place.models import Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    fields = ('title', 'address', 'logo', 'description', 'published')
    list_display = ('title', 'address', 'published')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'address')
