import json
import pprint
from customer import *

users = []
users_data = json.load(open('customers.json'))


def load_data():
    for data_row in users_data:
        users.append(Customer(data_row))

load_data()

print(len(users))

# for user in users:
#     print(user.is_at_distance_from(100, 53.339428, -6.257664))

u = filter(lambda user: user.is_at_distance_from(100, 53.339428, -6.257664), users)

print(len(list(u)))
