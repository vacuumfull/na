"""Admin models from Places app"""
from django.contrib import admin

from event.models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    pass
