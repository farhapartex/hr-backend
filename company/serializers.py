from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class CompanyMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name")