from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #additional attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

admin.site.register(UserProfile)
