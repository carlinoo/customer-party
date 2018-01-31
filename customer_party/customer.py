import math


class Customer:
    def __init__(self, data):
        self.latitude = float(data['latitude'])
        self.longitude = float(data['longitude'])
        self.id = data['user_id']
        self.name = data['name']


    # decorates the string output of the object
    def __str__(self):
        return ("user_id: " + str(self.id) + ", name: " + self.name)



    # Calculates the distance of the customer from certain location
    def distance_from(self, lat, lon):
        lat2, lon2 = lat, lon

        # get in radians
        lat1, lon1, lat2, lon2 = map(math.radians, [self.latitude, self.longitude, lat2, lon2])

        total_lon = lon2 - lon1
        total_lat = lat2 - lat1

        # We use haversine formula
        a = math.sin(total_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(total_lon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # Get in kilometers multiplying by the radius of the earth
        in_kilometers = 6371 * c


        return in_kilometers



    # Checks if the distance from a point is at $distance
    def is_at_distance_from(self, distance, lat, lon):
        return self.distance_from(lat, lon) <= distance
