#forms for users profile

from django import forms
from userprofile.models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = []

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = []