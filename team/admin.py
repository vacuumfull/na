from django.contrib import admin

from team.models import Team


@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
