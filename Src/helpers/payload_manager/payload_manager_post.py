from faker import Faker
import json
import jsonschema


def payload_post():
    faker = Faker()
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": str(faker.date_between(start_date='-3y', end_date='today')),
            "checkout": str(faker.date_between(start_date='today', end_date='+3y'))
        },
        "additionalneeds": faker.random_element(elements=('breakfast', 'Lunch', 'dinner'))
    }
    return payload

