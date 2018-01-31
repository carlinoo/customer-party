import json
import pprint
from customer import *

users = []
users_data = json.load(open('customers.json'))


def load_data():
    for data_row in users_data:
        users.append(Customer(data_row))

load_data()
