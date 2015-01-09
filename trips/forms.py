#forms for trips and reservations

from django import forms
from trips.models import Reservation, Trip

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        exclude = []

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        exclude = []