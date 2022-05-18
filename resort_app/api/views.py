from resort_app.models import *
from .serializers import *
from .permissions import *
from .throttling import *
from django.shortcuts import render
from rest_framework.throttling import AnonRateThrottle
from rest_framework import viewsets


# Create your views here.

class ResortViewSet(viewsets.ModelViewSet):
    queryset = Resort.objects.all()
    serializer_class = ResortSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_throttles(self):
        if self.action in ['list'] and not self.request.user.is_anonymous:
            throttle_classes = [ResortListThrottle]
        elif self.action in ['list'] and self.request.user.is_anonymous :
            throttle_classes = [AnonRateThrottle]
        return [throttle() for throttle in throttle_classes]
