from Src.Constants import api_constants as constants
from Src.helpers import requests
from Src.helpers.payload_manager import payload_manager_post as post_payload
from Src.helpers.utils import headers_json
def test_create():
    url=constants.URL.createbooking()
    json_payload=post_payload.payload_post()
    response = requests.post_request(url=url, headers=headers_json(),payload=json_payload)
    return response
