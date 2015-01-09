from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

TYPE_CHOICES = [
    ('flight', 'Flight'),
    ('hotel', 'Hotel'),
    ('car', 'Car')
]

SOURCE_CHOICES = [
    ('email', 'Email'),
    ('fwd_email', 'FWD_EMAIL'),
    ('user', 'USER')
]
"""
class ReservationManager(models.Manager):
    def create(self, **kwargs):
        allowed_attributes = {'source', 'type', 'original', 'destination', 'arr_datetime', 'dep_datetime', 'confirmation_num', 'brand', 'cost', 'location_name', 'address'}
        for name, value in kwargs.items():
            assert name in allowed_attributes
            setattr(self, name, value)
        self.save()
        return
"""   

class Trip(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    description = models.TextField()


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    trip_id = models.ForeignKey('Trip')
    source = models.CharField(choices=SOURCE_CHOICES, max_length=30)
    source_id = models.CharField(max_length=30)
    created =  models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    userid = models.ForeignKey(User)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    arr_datetime = models.DateTimeField(null=True)
    dep_datetime = models.DateTimeField(null=True)
    confirmation_num = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    cost = models.CommaSeparatedIntegerField(max_length=30)
    location_name = models.CharField(max_length=200)
    address = models.TextField()

    #object = ReservationManager()


admin.site.register(Reservation)
admin.site.register(Trip)