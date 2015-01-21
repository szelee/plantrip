from locations import *
from allauth.socialaccount.models import SocialApp
import json, requests
from datetime import date, datetime
from django.http import HttpResponseRedirect

#fsqr_venue_url = "https://api.foursquare.com/v2/venues/search"
today_date = date.today()

def fsqr_api(location):
    #save the result back to json file 
    #client id and client secret are stored in socialapp
    #https://api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=YYYYMMDD

    try:
        fsqr_app = SocialApp.objects.get(provider='foursquare')
        payload = {'near': location,
                   'client_id': fsqr_app.client_id,
                   'client_secret': fsqr_app.secret,
                   'v': '{:%Y%m%d}'.format(today_date)}

        response = requests.get(FSQR_VENUE_URL, params=payload)
        
        if response.status_code == 200:
            timestamp = datetime.utcnow()
            with open('fsqr_' + location + '_' + '{:%Y%m%d%H%M%S}'.format(timestamp) + '.json', 'w') as outfile:
                json.dump(response.json(), outfile)

    except Exception as e:
        print "Error in fsqr_api def: ", e

def gplaces_api(location):
    try:
        places_app = SocialApp.objects.get(name='places')
        payload = {'location': location,
                   'radius': 1000,
                   'key': places_app.client_id}

        response = requests.get(GPLACES_BASIC_URL, params=payload)

        if response.status_code == 200:
            timestamp = datetime.utcnow()
            with open('places_' + location + '_' + '{:%Y%m%d%H%M%S}'.format(timestamp) + '.json', 'w') as outfile:
                json.dump(response.json(), outfile)

    except Exception as e:
        print "Error in gplaces_api def: ", e







