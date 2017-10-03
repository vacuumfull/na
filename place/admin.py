"""Admin models from Places app"""
from django.contrib import admin

from place.models import Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    pass
