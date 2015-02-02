from django.db import models

# Create your models here.
PREF_CHOICES = [
    ('vintage_point', 'Vintage Point'),
    ('popular', 'Popular'),
    ('museum', 'Museum'),
    ('restaurant', 'Restaurant'),
    ('park', 'Park'),
    ('kids', 'Kids Friendly'),
    ('shopping', 'Shopping'),
    ('pub', 'Local Pub'),
    ('cafe', 'Cafe'),
    ('group', 'Group travel'),
    ('fast_food', 'Quick bite'),
    ('deal', 'Special Deal'),
    ('magic', 'Something Magic')
]


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    coordinate = models.CharField(max_length = 255)
    address = models.TextField()
    type = models.CharField(choices=PREF_CHOICES, max_length=150)
    operating_hr =  models.TextField()
    description = models.TextField()
    rating = models.IntegerField()

class Location_Attr(models.Model):
    location = models.ForeignKey('Location')

