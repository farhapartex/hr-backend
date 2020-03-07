from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass

@admin.register(Designation)
class Designation(admin.ModelAdmin):
    list_display = ("name","salary","experience")
