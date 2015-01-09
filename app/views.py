"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.core.context_processors import csrf
from app.forms import ContactForm
from app.models import ContactUs

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Start Here',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Customer Service',
            'message':'We are here for you',
            'contact': ContactUs.objects.all(),
            'year':datetime.now().year,
        })
    )
    #return render_to_response('app/contact.html',
    #                          {'contact' : ContactUs.objects.all()}
    #                          )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About Us',
            'message':'A small company',
            'year':datetime.now().year,
        })
    )
