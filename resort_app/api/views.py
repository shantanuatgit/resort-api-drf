from resort_app.models import *
from .serializers import *
from .permissions import *
from .throttling import *
from django.shortcuts import render
from rest_framework.throttling import AnonRateThrottle
from rest_framework import viewsets, generics, mixins
from rest_framework import filters

# Create your views here.

class ResortViewSet(viewsets.ModelViewSet):
    queryset = Resort.objects.all()
    serializer_class = ResortSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['resort_name', 'street', 'town__town_name']
    ordering_fields = ['star_rating']

    def get_throttles(self):
        if self.action in ['list'] and not self.request.user.is_anonymous:
            throttle_classes = [ResortListThrottle]
        elif self.action in ['list'] and self.request.user.is_anonymous :
            throttle_classes = [AnonRateThrottle]
        return [throttle() for throttle in throttle_classes]


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['town__town_name', 'town__state']

    def get_throttles(self):
        if self.action in ['list'] and not self.request.user.is_anonymous:
            throttle_classes = [PointofInterestThrottle]
        elif self.action in ['list'] and self.request.user.is_anonymous :
            throttle_classes = [AnonRateThrottle]
        return [throttle() for throttle in throttle_classes]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAdminOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city']


class ManagerDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsOwnerOrAdminOnly]

    def get(self, request, pk):
        return self.retrieve(request,pk)


class GuestList(generics.ListAPIView,
                generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsManagerOnly]


class GuestDetail(mixins.RetrieveModelMixin,
                generics.GenericAPIView):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsOwnerOrManagerOnly]
    throttle_classes = [GuestDetailThrottle]

    def get(self, request, pk):
        return self.retrieve(request,pk)
