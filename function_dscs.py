from random import choice
from math import cos, asin, sqrt, pi
import requests
import pandas as pd
import ast

YOUR_API_KEY = 'AIzaSyAfJ_mnFwaB__jjZ4Ll9aVBCfVNehcQVpYs'

def route(origin, destination, mode='walking', api_key = YOUR_API_KEY):
    url = "https://maps.googleapis.com/maps/api/directions/json?"+\
        "origin=" + origin + \
        "&destination=" + destination + \
        '&mode=' +  mode + \
        "&key=" + YOUR_API_KEY \

    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response.json
    data = response.json() 

    locations = [i['start_location'] for i in data['routes'][0]['legs'][0]['steps']] +\
                    [data['routes'][0]['legs'][0]['steps'][-1]['end_location']]
    duration = sum([data['routes'][0]['legs'][0]['steps'][i]['duration']['value'] for 
                    i in range(len(data['routes'][0]['legs'][0]['steps']))])  # in seconds

    return (locations, duration)

def distance(lat1, lon1, lat2, lon2): # in km
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

def algo(origin, destination, mode='walking', max_distance=1.000, interests=['cafe', 'bar']):
    shortest_route = route(origin= origin, destination= destination, mode='walking')
    poi = pd.read_csv('poi.txt') # structure: 'name', 'category', 'coordinates'
    poi['2'] =  poi['2'].map(lambda d : ast.literal_eval(d))

    res = [(j[0],j[2], min([distance(i['lat'], i['lng'], j[2]['lat'], j[2]['lng']) for i in shortest_route[0]])) 
           for j in poi.values if j[1] in interests]

    choice_poi = choice(res)
    waypoint = str(choice_poi[1]['lat']) + ',' + str(choice_poi[1]['lng']) 
    first_part = route(origin= origin, destination= waypoint, mode=mode)
    second_part = route(origin= waypoint, destination= destination, mode=mode)

    proposed_route = first_part[0][:-1] + second_part[0]
    duration = first_part[1] + second_part[1]
    
    result = {'begin_point': origin, 
            'end_point': destination, 
            'POI':choice_poi[0], 
            'route':proposed_route, 
            'mode':mode, 
            'duration':duration}
    return result


