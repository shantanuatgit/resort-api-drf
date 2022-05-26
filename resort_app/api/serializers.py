from ..models import *
from rest_framework import serializers


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class ResortSerializer(serializers.ModelSerializer):
    town = TownSerializer(read_only=True)
    manager = serializers.CharField(source='manager.name')

    class Meta:
        model = Resort
        fields = '__all__'


class PointOfInterestSerializer(serializers.ModelSerializer):
    town = TownSerializer(read_only=True)

    class Meta:
        model = PointOfInterest
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    guest_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Guest
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviews_guest = serializers.CharField(source='guest.name')
    reviews_resort = serializers.CharField(source='resort.resort_name')

    class Meta:
        model = Review
        fields = '__all__'


class CabinSerializer(serializers.ModelSerializer):
    cabin_resort = serializers.CharField(source='resort.resort_name')

    class Meta:
        model = Cabin
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    booking_guest = GuestSerializer(many=True, read_only=True)
    booking_cabin = CabinSerializer(many=True, read_only=True)
    booking_resort = serializers.CharField(source='resort.resort_name')

    class Meta:
        model = Booking
        fields = '__all__'

class CabinCostSerializer(serializers.ModelSerializer):
    cabin_cost_resort = serializers.CharField(source='resort.resort_name')
    class Meta:
        model = CabinCost
        fields = '__all__'
