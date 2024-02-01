import openpyxl
import requests
from Src.helpers.utils import headers_json
import json
def read_xl(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username":username,
                            "password":password})
    return credentials

def make_request(username,password):
    payload={
        "username": username,
        "password": password
    }
    url="https://restful-booker.herokuapp.com/auth"
    response=requests.post(url=url,headers=headers_json(),auth=None,json=payload)
    return response


def test_token():
    file_path="C:\\Users\\rajes\\PycharmProjects\\SelfEvalution.py\\Src\\resources\\Untitled spreadsheet.xlsx"
    credentials=read_xl(file_path)
    for user_cred in credentials:
        username=user_cred["username"]
        password=user_cred["password"]
        response=make_request(username,password)
        json_response=response.json()
        try:
            token = json_response['token']
            print(username, password)
        except KeyError as e:
            pass
    return token
