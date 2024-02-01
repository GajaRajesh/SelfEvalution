from Src.Constants.api_constants import URL
from Tests.Basic_Tests.test_create_booking import test_create
from Src.helpers import requests
from dotenv import load_dotenv
from Src.helpers.utils import headers_json
from Src.helpers.payload_manager.payload_manager_put import payload_put
import os
def test_updtae():
    load_dotenv()
    cresponse = test_create().json()
    id=cresponse["bookingid"]
    url=URL.updatebooking(id)
    username =os.getenv("Name")
    password =os.getenv("password")
    response = requests.put_request(
        url=url,usr=username,pwd=password,
        headers=headers_json(),payload=payload_put())
    return response

