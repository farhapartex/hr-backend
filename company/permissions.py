from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from system.permissions import _check_has_permission
from .models import *


class CompanyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return _check_has_permission(request,Company, view)

    
    def has_object_permission(self, request, view, obj):
        return _check_has_permission(request,Company, view)
            