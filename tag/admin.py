from django.contrib import admin

from tag.models import Tag

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    """Tags admin page."""
    pass
