from resort_app.models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

class ResortViewSet(viewsets.ModelViewSet):
    queryset = Resort.objects.all()
    serializer_class = ResortSerializer
