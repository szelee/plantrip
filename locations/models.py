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
    Name = models.CharField(max_length = 255)
    coordinate = models.CharField(max_length = 255)
    Address = []
    subject = models.CharField(max_length=150)
    message =  models.TextField()