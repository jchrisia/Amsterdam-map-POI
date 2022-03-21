from function_dscs import algo


# example

origin = 'Kerkstraat 193,Amsterdam'
destination = 'Science_Park_campus,Amsterdam'
mode = 'walking'  # or   or 'walking'
max_distance = 1.000 # 1000 meters
interests = ['cafe', 'bar'] # interests; options: cafe, bar, restaurant, tourist_attraction, park, point_of_interest


res = algo(origin = origin, 
           destination = destination,
           mode = mode, 
           max_distance = max_distance, 
           interests = interests)

res.keys()  # dict_keys(['begin_point', 'end_point', 'POI', 'route', 'mode', 'duration'])

for i in res['route']:
    i