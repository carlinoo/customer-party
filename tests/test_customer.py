from customer_party import Customer
from math import *
import pytest

# Creating of customer to use in test
customer = Customer({"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})


# Test that customer is created properly
def test_customer_creation():

    condition = (customer.latitude == 52.986375 and customer.id == 12 and customer.name == "Christina McArdle" and customer.longitude == -6.043701)

    assert condition


# Test that customer is printed property to the console
def test_customer_to_str():
    assert str(customer) == "user_id: 12, name: Christina McArdle"


# Test a distance from the customer to a points (54, -9)
def test_customer_distance_from_1():
    assert floor(customer.distance_from(54, -9)) == 225



# Test a distance from the customer to a points (57, -8)
def test_customer_distance_from_2():
    assert floor(customer.distance_from(57, -8)) == 463



# Test a distance from the customer to a points (51, -2)
def test_customer_distance_from_3():
    assert floor(customer.distance_from(51, -2)) == 354


# Test that is_at_distance_from works (distance of customer to (51, -2) is 354.08)
def test_customer_is_at_distance_from():
    assert customer.is_at_distance_from(355, 51, -2) and not customer.is_at_distance_from(354, 51, -2)


# Test a TypeError is raised when getting distance passsing a string
def test_customer_distance_from_type_error():
    with pytest.raises(TypeError):
        assert floor(customer.distance_from('51', -2)) == 354 and floor(customer.distance_from(51, '-2')) == 354
