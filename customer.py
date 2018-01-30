class Customer:
    def __init__(self, data):
        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.id = data['user_id']
        self.name = data['name']

        def __str__(self):
            return str("user_id: " + self.id + ", latitude: " + self.latitude + ", longitude: " + self.longitude + ", name: " + self.name)

        def __repr__(self):
            return __str__(self)
