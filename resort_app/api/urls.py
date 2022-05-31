"""resort_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from resort_app.api import views

router = DefaultRouter()
router.register('resorts', views.ResortViewSet, basename='resorts')
router.register('poi', views.PointOfInterestViewSet, basename='poi')
router.register('managers', views.ManagerViewSet, basename='managers')

urlpatterns = [
    path('', include(router.urls)),
    path('manager/<int:pk>/', views.ManagerDetail.as_view(), name='manager-detail'),

    path('guests/<int:pk>/', views.GuestDetail.as_view(), name='guest-detail'),
    path('guests/', views.GuestList.as_view(), name='guest-list'),

    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
    path('<int:pk>/bookings/', views.BookingCreate.as_view(), name='booking-create'),
]
