from Tests.Basic_Tests.test_create_booking import test_create
from Tests.Basic_Tests.test_update_booking import test_updtae
from Tests.Basic_Tests.test_pupdate_booking import test_pupdate
from Tests.Basic_Tests.test_get_booking import test_get
from Src.helpers.utils import load_schema
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def test_json_validator_create():
    response = test_create()
    json_response = response.json()
    file = "C:\\Users\\rajes\\PycharmProjects\\SelfEvalution.py\\Src\\resources\\test_create.json"
    schema = load_schema(file)
    try:
        validate(instance=json_response, schema=schema)
    except ValidationError as e:
        print(e)


def test_json_validator_Fullupdate():
    response = test_updtae()
    json_response = response.json()
    file = "C:\\Users\\rajes\\PycharmProjects\\SelfEvalution.py\\Src\\resources\\test_fullupdate.json"
    scheama = load_schema(file)
    try:
        validate(instance=json_response, schema=scheama)
    except ValidationError as e:
        print(e)


def test_json_validate_partialupdate():
    response=test_pupdate()
    json_response=response.json()
    file = "C:\\Users\\rajes\\PycharmProjects\\SelfEvalution.py\\Src\\resources\\test_fullupdate.json"
    schema=load_schema(file)
    try:
        validate(instance=json_response,schema=schema)
    except ValidationError as e:
        print(e)


def test_json_validate_get():
    response=test_get()
    json_response=response.json()
    file = "C:\\Users\\rajes\\PycharmProjects\\SelfEvalution.py\\Src\\resources\\test_fullupdate.json"
    schema=load_schema(file)
    try:
        validate(json_response,schema)
    except ValidationError as e:
        print(e)
