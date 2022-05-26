from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_manager',
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_manager',
                'groups', 'user_permissions',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        # ('Additional info', {
        #     'fields': ('is_manager',)
        # })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_manager',
                'groups', 'user_permissions',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        # ('Additional info', {
        #     'fields': ('is_manager',)
        # })
    )
admin.site.register(CustomUser, CustomUserAdmin)
