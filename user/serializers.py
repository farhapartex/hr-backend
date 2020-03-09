from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from .models import *

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class GroupMinimalSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, model):
        return model.permissions.all().count()

    class Meta:
        model = Group
        fields = ("id", "name", "count")

class GroupSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Group
        fields = "__all__"