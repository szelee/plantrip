# Create your views here.

from django.shortcuts import render, render_to_response
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from userprofile.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        #user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

        else:
            print profile_form.errors

    else:
        profile_form = UserProfile()

    return render(
        request,
        'userprofile/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Welcome back, ' + request.user.first_name,
            'message':'Where do you want to explore today?',
            'userprofile': profile_form,
            'user': request.user,
            'year':datetime.now().year,
        })
    )