import os
import json
import requests

url = "https://fakestoreapi.com/products"

save_path = './data'
file_name = "general.json"

completeName = os.path.join(save_path, file_name)

response = requests.request("GET", url)

with open(completeName, 'w') as json_file:
    json.dump(response.json(), json_file)