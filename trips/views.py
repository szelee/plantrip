# Create your views here.

from django.shortcuts import render, render_to_response
from trips.models import Trip, Reservation
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from trips.forms import ReservationForm, TripForm
from django.core.context_processors import csrf
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def alltrips(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'trips/trip.html',
        context_instance = RequestContext(request,
        {
            'title':'Trips',
            'message':'All the trips with Well,PlanForMe',
            'trips': Trip.objects.all(),
            'year':datetime.now().year,
        })
    )

@login_required
def createtrip(request):
    if request.POST:
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/trip/all')
    else:
        form = TripForm()

    #args = {}
    #args.update(csrf(request))
    #args['form'] = form
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'trips/create_trip.html',
        context_instance = RequestContext(request,
        {
            'title':'Start Here',
            'message':'Plan your trip here',
            'form': form,
            'year':datetime.now().year,
        })
    )
    #return render_to_response('trips/create_trip.html', args)
