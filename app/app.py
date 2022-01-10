import os
import json
import requests

fakerUrl = "https://fakestoreapi.com/products"
demoUrl = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
url = demoUrl

save_path = './data'
file_name = "general.json"

completeName = os.path.join(save_path, file_name)

response = requests.request("GET", url)

with open(completeName, 'w') as json_file:
    json.dump(response.json(), json_file)
