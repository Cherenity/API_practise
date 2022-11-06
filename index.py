import requests
import json
import geopy.distance


# request data from snowplowAPI and returns it in json
def fetch_data():
    response_API = requests.get('http://dev.hel.fi/aura/v1/snowplow/')
    data = response_API.json()
    return data

# returns a unique set of plows from the data
def list_all_snowplows(data):
    unique_plows = set(())
    for key in data:
        unique_plows.add(key['id'])
    return(unique_plows)

# returns a unique set of recent activities from the data
def list_all_recent_activities(data):
    unique_activities = set(())
    for key in data:
        unique_activities.add(key['last_location']['events'][0])
    return(unique_activities)

# compares data to user location and returns the closest result
def get_closest_location(data, user_location):
    closest_result = ()
    shortest_distance = -1
    
    for key in data:
        location = key['last_location']['coords']
        key_location = (str(location[1]), str(location[0]))
        distance = geopy.distance.geodesic(key_location, user_location).km
               
        if shortest_distance == -1:
            shortest_distance = distance
            closest_result = key
        
        elif distance < shortest_distance:
            shortest_distance = distance
            closest_result = key
    
    return closest_result

def get_coordinates(key):
    location = key['last_location']['coords']
    key_location = (str(location[1]), str(location[0]))
    return key_location


# displays location on map from given coordinates
def display_location_on_map(coords):
    print("http://www.google.com/maps/place/" + str(coords[0])+","+str(coords[1]))

def main():
    # default user location, in front of Ateneum
    user_location = (60.17028754851743, 24.944031808695787)
    
    data = fetch_data()
    # closest = get_closest_location(data,user_location)

    

    print("BAJJU")


if __name__ == "__main__":
    main()

    

# http://dev.hel.fi/aura/v1/snowplow/5407?history=50
# The query above will display information about plow 5407 with 50 previous locations included.

# snowplow = data[0]['last_location']['coords']
# coords = str(snowplow[1]) + ',' + str(snowplow[0])

# coords_2 = (snowplow[1], snowplow[0])
# print(coords)


# print("http://www.google.com/maps/place/" + coords)
# print(data[0]['last_location']['events'])

# Distance between locations
# print(geopy.distance.geodesic(coords_1, coords_2).km)