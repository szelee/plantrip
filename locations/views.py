# Create your views here.
from collections import namedtuple
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from locations.getlocations import get_location

import simplejson, json

from locations import *


def search(request):
    location = request.POST.get('searchplace')
    geolocation = request.POST.get('searchgeoloc')

    #f = open(fsqr_json_file, 'r')
    #data = json.load(f)
    #shop = data['response']['venues']
    #f.close()
    print location
    fsqr_shops = get_location('foursquare', location)

    assert isinstance(request, HttpRequest)
    return render(
        request,
        "locations/home.html",
        context_instance = RequestContext(request,
        {
            'title': location,
            'message': 'Recommended places gathered from different website',
            'year':datetime.now().year,
            'shop': fsqr_shops,
            #'fsqr': fsqr_shops,
        })
    )