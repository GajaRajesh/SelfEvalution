from faker import Faker


def payload_pupdate():
    faker = Faker()
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name()
    }
    return payload
