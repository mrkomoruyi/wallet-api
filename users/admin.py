from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'usable_password', 'password1', 'password2', 'email', 'first_name', 'last_name'),
            },
        ),
    )