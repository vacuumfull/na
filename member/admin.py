from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from member.models import UserExtend, UserSettings

admin.site.unregister(User)


class UserExtendInline(admin.TabularInline):
    model = UserExtend
    can_delete = False
    verbose_name_plural = 'аватар и социальные сети'


class UserSettingInline(admin.TabularInline):
    model = UserSettings
    can_delete = False
    verbose_name_plural = 'настройки пользователя'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Основные сведения', {
            'fields': (
                'username', 'email', 'first_name', 'last_name', 'password')}),
        ('Информация', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Базовые настройки', {
            'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
    inlines = (UserExtendInline, UserSettingInline)
    readonly_fields = ('last_login', 'date_joined')
