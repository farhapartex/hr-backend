from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from system.permissions import _check_has_permission
from .models import *

class IsSuperAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_superuser


class GroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return _check_has_permission(request,Group, view)

    
    def has_object_permission(self, request, view, obj):
        return _check_has_permission(request,Group, view)
            

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return _check_has_permission(request, User, view)

    
    def has_object_permission(self, request, view, obj):
        return _check_has_permission(request,User, view)
            