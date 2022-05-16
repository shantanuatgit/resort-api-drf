from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Town(models.Model):
    town_name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    summer_temp = models.FloatField()
    winter_temp = models.FloatField()
    sealevel = models.FloatField()


class Manager(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)


class Resort(models.Model):
    resort_name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    town_name = models.CharField(max_length=30)
    star_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='resort_town')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='resort_manager')


class PointofInterest(models.Model):
    describes = models.CharField(max_length=30)
    open_time = models.CharField(max_length=30)
    close_time = models.CharField(max_length=30)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='poi_town')


class Guest(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=320)
    email = models.EmailField()
    phone = models.CharField(max_length=10)


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reviews_guest')
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='reviews_resort')


class Cabin(models.Model):
    describes = models.CharField(max_length=30)
    cabin_type = models.CharField(max_length=10)
    bedroom_count = models.PositiveIntegerField()
    sleep_capacity = models.PositiveIntegerField()
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='cabin_resort')


class Booking(models.Model):
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    adult_count = models.PositiveIntegerField()
    child_count = models.PositiveIntegerField()
    pet_count = models.PositiveIntegerField()
    total_charge = models.PositiveIntegerField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='booking_guest')
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='booking_resort')
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE, related_name='booking_cabin')


class CabinCost(models.Model):
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    rate = models.PositiveIntegerField()
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='cabin_cost_resort')
