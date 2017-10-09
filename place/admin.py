"""Admin models from Places app"""
from django.contrib import admin

from place.models import Location, Place


class LocationInLine(admin.StackedInline):
    """InLine admin model locations for Places."""

    model = Location
    extra = 1


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    fields = ('title', 'image', 'icon', 'description', 'owner', 'published',
              'musicians')
    inlines = [LocationInLine]
    list_display = ('title', 'published')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'address')
