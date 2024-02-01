from Src.Constants.api_constants import URL
from Src.helpers.requests import get_request
from Tests.Basic_Tests.test_create_booking import test_create
from Src.helpers.utils import headers_json
def test_get():
    id=test_create().json()["bookingid"]
    print(id)
    url=URL.getbooking(id)
    print(url)
    response=get_request(URL=url,headers=headers_json())
    return response
