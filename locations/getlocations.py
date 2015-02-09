from locations import *
from allauth.socialaccount.models import SocialApp
import json, requests
from datetime import date, datetime
from django.http import HttpResponseRedirect
from factual import Factual

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

    elif provider == 'factual':
        data = factual_api(location)
        shops = data

    return shops

def factual_api(location):
    factual = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    location = 'london'
    #SLL - temporary commented schema as prototype will get the information immediately from the factaul db
    #s = factual.table('places').schema()
    
    places = factual.table('places')
    popular = places.filters({'$and':[{'category_ids':{'$includes_any':[107,308,371]}},{'locality': location}]}).sort({'placerank':800}).data()
    restaurant = places.filters({'$and':[{'category_ids':{'$includes_any':[312,338]}},{'locality': location}]}).sort({'placerank':1000}).data()
    to_do = places.filters({'$and':[{'category_ids':{'$includes_any':[317,147,169]}},{'locality': location}]}).sort({'placerank':1000}).data()

    #f = open('locations\popular_places.json', 'r')
    #popular = json.load(f)
    #restaurant = {}
    #to_do = {}

    result = {}
    result['popular'] = popular
    result['restaurant'] = restaurant
    result['to_do'] = to_do
    
    return result






