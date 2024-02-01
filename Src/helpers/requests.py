import requests
import json
from requests.auth import HTTPBasicAuth

def post_request(url,headers,payload):
    response=requests.post(url=url, headers=headers, json=payload)
    return response

def get_request(URL,headers):
    response=requests.get(url=URL,headers=headers)
    return response

def put_request(url,usr,pwd,headers,payload):
    response = requests.put(url=url, auth=HTTPBasicAuth(usr,pwd),
                          headers=headers, json=payload)
    return response

def patch_request(URL,usr,pwd,headers,payload):
    response=requests.patch(url=URL,data=json.dumps(payload),headers=headers,
                            auth=HTTPBasicAuth(username=usr,password=pwd))
    return response

def delete_request(URL,usr,pswd,headers):
    response=requests.delete(url=URL,headers=headers,
                             auth=HTTPBasicAuth(username=usr,password=pswd))
    return response