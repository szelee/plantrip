from locations import *
from allauth.socialaccount.models import SocialApp
import json, requests
from datetime import date, datetime
from django.http import HttpResponseRedirect
from factual import Factual

today_date = date.today()

def fsqr_api(location):
    #save the result back to json file 
    #client id and client secret are stored in socialapp
    #https://api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=YYYYMMDD
    #https://api.foursquare.com/v2/venues/explore?v=20131016&ll=51.500152%2C-0.126236&section=food&novelty=new&venuePhotos=1

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

    if provider == 'factual':
        data = factual_api(location)
        shops = data

    return shops

def factual_api(location):
    factual = Factual(FACTUAL_KEY, FACTUAL_SECRET, timeout=60.0)
    location = 'london'
    #SLL - temporary commented schema as prototype will get the information immediately from the factaul db
    #s = factual.table('places').schema()
    
    #places = factual.table('places')
    #popular = places.filters({'$and':[{'category_ids':{'$includes_any':[107,308,371]}},{'category_ids': {'$excludes_any':[62,177,430, 347]}},{'locality': location}]}).sort({'placerank':1000}).data()
    #restaurant = places.filters({'$and':[{'category_ids':{'$includes_any':[312,347, 338]}},{'locality': location}]}).sort({'placerank':1000}).data()
    #to_do = places.filters({'$and':[{'category_ids':{'$includes_any':[317,147,169]}},{'locality': location}]}).sort({'placerank':1000}).data()

    #f = open('locations\popular_places.json', 'r')
    #popular = json.load(f)
    popular = process_photos(explore_fsqr())
    restaurant = {}
    to_do = {}

    result = {}
    result['popular'] = popular
    result['restaurant'] = restaurant
    result['to_do'] = to_do
    
    return result

def download_factual_category():
    factual = Factual(FACTUAL_KEY, FACTUAL_SECRET, timeout=60.0)
    places_schema = factual.table('places').schema()
    
    filename = 'locations/factual_cat_schema.json'
    with open(filename, 'w') as outfile:
        json.dump(places_schema, outfile)
        outfile.close()

def explore_fsqr():
    
    f = open('locations/fsqure_explore_london.json', 'r')
    places = json.load(f, 'ISO-8859-1')
    f.close()

    return places

def trending_fsqr():

    f = open('locations/fsqr_trending.json', 'r')
    places = json.load(f, 'ISO-8859-1')
    f.close()

    return places

def process_photos(places):

    if places:
        for place in places:
            if place['venue']['featuredPhotos']:
                place['venue']['photos']['photoBig'] = place['venue']['featuredPhotos']['items'][0]['prefix'] + "110x110" + place['venue']['featuredPhotos']['items'][0]['suffix']
            elif place['venue']['photos']:
                place['venue']['photos']['photoBig'] = place['venue']['photos']['items'][0]['prefix'] + "110x110" + place['venue']['photos']['items'][0]['suffix']

    return places