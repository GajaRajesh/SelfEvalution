from Src.Constants.api_constants import URL
from Src.helpers.requests import delete_request
from Tests.Basic_Tests.test_create_booking import test_create
from dotenv import load_dotenv
import os
from Src.helpers.utils import headers_json
def test_delete():
    load_dotenv()
    id=test_create().json()["bookingid"]
    url=URL().delete(id)
    username=os.getenv('NAME')
    password=os.getenv('PASSWORD')
    response=delete_request(URL=url,usr=username,pswd=password,headers=headers_json())
    print(response.text)