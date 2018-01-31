import json
from customer import Customer

# Load data from JSON and return it as object
def load_data_from(location):
    users = []
    for data_row in json.load(open(location)):
        users.append(Customer(data_row))
    return users


# Function that will filter out the customers within 100 km from our Dublin office
def filter_customers(customers_array):
    u = filter(lambda customer: customer.is_at_distance_from(100, 53.339428, -6.257664), customers_array)
    return u


# Function to run the program
def run():
    # Load the JSON File
    customers = load_data_from('../customers.json')

    # Filter out the customers
    customers = filter_customers(customers)

    # We sort the customers in ascending order by the id of them
    customers = sorted(customers, key = lambda customer: customer.id)

    # print all the filtered and ordered customers
    for customer in customers:
        print(customer)


# Run the program
run()
