import json
import requests

url = "https://fakestoreapi.com/products"

def jprint(obj):
    # create a formatted string of the Python JSON object
    jsonData = json.dumps(obj, sort_keys=True, indent=4)
    print(jsonData)
    return jsonData

response = requests.request("GET", url)

if(response.status_code == 200):
    jsonResponse = jprint(response.json())
    with open('demo.json', 'w') as json_file:
        json.dump(jsonResponse, json_file)
