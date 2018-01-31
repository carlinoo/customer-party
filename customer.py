from math import *


class Customer:
    def __init__(self, data):
        self.latitude = float(data['latitude'])
        self.longitude = float(data['longitude'])
        self.id = data['user_id']
        self.name = data['name']


    # decorates the string output of the object
    def __str__(self):
        return ("user_id: " + str(self.id) + ", latitude: " + self.latitude + ", longitude: " + self.longitude + ", name: " + self.name)



    # Calculates the distance of the customer from certain location
    def distance_from(self, lat, lon):
        lat2, lon2 = lat, lon

        lat1, lon1, lat2, lon2 = map(radians, [self.latitude, self.longitude, lat2, lon2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))

        km = 6371* c

        return km



    # Checks if the distance from a point is at $distance
    def is_at_distance_from(self, distance, lat, lon):
        return self.distance_from(lat, lon) <= distance
