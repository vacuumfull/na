from django.contrib import admin

from place.models import Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
