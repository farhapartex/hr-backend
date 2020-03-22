from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from .models import *

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class GroupMinimalSerializer(serializers.ModelSerializer):
    total_permission = serializers.SerializerMethodField()
    total_user = serializers.SerializerMethodField()

    def get_total_permission(self, model):
        return model.permissions.all().count()

    def get_total_user(self, model):
        return model.user_set.count()

    class Meta:
        model = Group
        fields = ("id", "name", "total_permission", "total_user")

class GroupSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Group
        fields = "__all__"

class EmployeeMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "branch", "designation", "joining_date",)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class UserEmployeeMinimalSerializer(serializers.ModelSerializer):
    employee = EmployeeMinimalSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "image", "employee")

class UserMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "image",)
