"""
Definition of models.
"""

from django.db import models

# Create your models here.

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    sender = models.EmailField()
    subject = models.CharField(max_length=150)
    message =  models.TextField()
