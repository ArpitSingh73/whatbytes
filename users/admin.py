from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser  # or CustomUser


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active")


admin.site.register(CustomUser, CustomUserAdmin)
