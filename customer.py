class Customer:
    def __init__(self, data):
        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.id = data['user_id']
        self.name = data['name']

    def __str__(self):
        return ("user_id: " + str(self.id) + ", latitude: " + self.latitude + ", longitude: " + self.longitude + ", name: " + self.name)
