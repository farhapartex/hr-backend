from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class CompanyAPIViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, CompanyPermission)

    def get_serializer_class(self):
        return CompanyMinimalSerializer if self.action == "list" else CompanySerializer