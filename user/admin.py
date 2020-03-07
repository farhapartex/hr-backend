from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_superuser", "is_staff", "last_login", "is_active")
