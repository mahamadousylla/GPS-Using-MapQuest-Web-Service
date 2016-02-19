#Mahamadou Sylla 61549479

import urllib.parse
import urllib.request
import json

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key=Ty4mO3IWhIGPvcp4RaALftDXorf3Kl6G&'
elevation = 'http://open.mapquestapi.com/elevation/v1/profile?key=Ty4mO3IWhIGPvcp4RaALftDXorf3Kl6G&'

def build_url(locations):
    '''
    take in a list of locations, builds and and returns a URL that can
    be used to ask the MapQuest API for directions on a specific search
    '''
    destination = [('from', str(locations[0])) ] #a tuple consisting of the search that is to be made with the starting location listed first
    for location in locations[1:]: #for each location after the starting point
        destination.append(('to', str(location))) #appends this tuple for each 'to' location to destinations list
    parsed_query = urllib.parse.urlencode(destination) #parses the finished destination list that consists of the search query
    return BASE_MAPQUEST_URL + parsed_query #return the complete url


def get_result(url):
    '''
    takes in a URL and returns a Python object representing the
    parsed JSON response
    '''

    response = None #sets response equal to None
    try:
        response = urllib.request.urlopen(url) #makes an HTTP request and opens the given url
        json_text = response.read().decode(encoding = 'utf-8') #opens and reads the url and turns it into JSON format
        return json.loads(json_text) #turns the text into a JSON object 

    finally:
        if response != None: #if response is no longer equal to None, meaning the 'try' worked
            response.close() #close the response


def elevation_url(json_object):
        '''
        takes in a json_object, take the latitude and longitude for each location
        specified for a specific trip and uses that to build a url to get information about that locations elevation.
        Does this for each location specified for a specific trip and adds them all to a list
        '''
        result = [ ]
        for dictionary in json_object['route']['locations']: #access dictinary and the latitude and longitute fields
            search_query = [('shapeFormat', 'raw'), ('latLngCollection', str(dictionary['latLng']['lat'])+ ',' + str(dictionary['latLng']['lng']))] #parameters that need to be encoded
            parsed = urllib.parse.urlencode(search_query) #parameters are encoding and ready to be added to a complete URL
            url = elevation + parsed #URL is completed and ready to be used
            json_result = get_result(url) #reads the url and turns data recieved into a Python object
            for subdict in json_result['elevationProfile']: #for the subdict in this dictionary
                result.append(subdict['height']) #print the elevation
        return result #leaves the function

