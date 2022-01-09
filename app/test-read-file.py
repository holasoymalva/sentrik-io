import os
import json

save_path = './data'
file_name = "general.json"

completeName = os.path.join(save_path, file_name)

with open(completeName, 'r') as openfile:
    json_object = json.load(openfile)

# print(json_object)
print(type(json_object))
print(json_object[0]['title'])