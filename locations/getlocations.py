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
        payload = {'ll': location,
                   'client_id': fsqr_app.client_id,
                   'client_secret': fsqr_app.secret,
                   'v': '{:%Y%m%d}'.format(today_date)}

        response = requests.get(FSQR_VENUE_URL, params=payload)
        
        if response.status_code == 200:
            timestamp = datetime.utcnow()
            #file_name = 'fsqr_' + location + '_' + '{:%Y%m%d%H%M%S}'.format(timestamp) + '.json'
            #with open(file_name, 'w') as outfile:
            #    json.dump(response.json(), outfile)
            #outfile.close()
            return response.json()

    except Exception as e:
        print "Error in fsqr_api def: ", e

def gplaces_api(location):
    try:
        places_app = SocialApp.objects.get(name='places')
        print places_app.client_id

        payload = {'location': location,
                   'radius': 500,
                   'key': places_app.client_id}

        response = requests.get(GPLACES_BASIC_URL, params=payload)

        if response.status_code == 200:
            #timestamp = datetime.utcnow()
            #file_name = 'places_' + location + '_' + '{:%Y%m%d%H%M%S}'.format(timestamp) + '.json'
            #with open(filename, 'w') as outfile:
            #    json.dump(response.json(), outfile)
            #outfile.close()
            return response.json()

    except Exception as e:
        print "Error in gplaces_api def: ", e

def get_location(provider, location):
    #f = open(file_path, 'r')
    #data = json.load(f)

    if provider == 'foursquare':
        data = fsqr_api(location)
        shops = data['response']['venues']

    elif provider == 'google':
        data = gplaces_api(location)
        shops = data['results']
        print data
        print shops

    return shops







