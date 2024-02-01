import jsonschema
import json
def headers_json():
    headers={
        "Content-Type":"application/json"
    }
    return headers

def load_schema(schema_file):
    with open(schema_file,'r') as file:
        return json.load(file)
