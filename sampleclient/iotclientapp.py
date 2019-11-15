"""
Import the json and requests modules
"""
import json
import requests


# Define ML server url
URL = 'http://10.10.20.51:40000'

# Define the sample input
DATA = {'hour': 3
       }

DATA = json.dumps(DATA)
SEND_REQUEST = requests.post(URL, DATA)

# Print the post result
print(SEND_REQUEST)
# Print the model’s prediction output
print(SEND_REQUEST.json())
