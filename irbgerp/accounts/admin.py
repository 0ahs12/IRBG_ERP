from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_approved')

admin.site.register(CustomUser, CustomUserAdmin)
