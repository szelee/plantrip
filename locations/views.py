# Create your views here.
from collections import namedtuple
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

import simplejson, json

from locations import *


def search(request, location):
    f = open(fsqr_json_file, 'r')
    data = json.load(f)
    shop = data['response']['venues']
    f.close()
    #data = {'hello': ['world', 'universe']}
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "locations/home.html",
        context_instance = RequestContext(request,
        {
            'title': location,
            'year':datetime.now().year,
            'shop': shop,
        })
    )