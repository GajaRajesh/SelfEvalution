from Src.Constants.api_constants import URL
from Src.helpers.requests import patch_request
from Tests.Basic_Tests.test_create_booking import test_create
import os
from dotenv import load_dotenv
from Src.helpers.utils import headers_json
from Src.helpers.payload_manager.payload_manager_pupdate import payload_pupdate

def test_pupdate():
    load_dotenv()
    id = test_create().json()["bookingid"]
    url=URL().partial_update(id=id)
    username=os.getenv("NAME")
    password=os.getenv("PASSWORD")
    response=patch_request(URL=url,
                           usr=username,pwd=password,
                           headers=headers_json(),
                           payload=payload_pupdate())
    return response
