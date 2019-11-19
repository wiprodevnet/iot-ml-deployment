"""
Import the json and requests modules
"""
import json
import requests
from sample_data import PAYLOAD, FOG_APP_IP

# Define ML server url
URL = 'http://' + FOG_APP_IP

#Read json data
DATA = json.dumps(PAYLOAD)
print('{input:', DATA, '}')

#Poat the json payload data to ML server URL
SEND_REQUEST = requests.post(URL, DATA)

# Print the post result
print(SEND_REQUEST)
# Print the model’s prediction output
print(SEND_REQUEST.json())
