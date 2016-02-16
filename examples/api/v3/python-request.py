# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os

BASE_URL = 'https://api.tnyu.org/v3'
TEST_BASE_URL = 'https://api.tnyu.org/v3-test'

headers = {
    'content-type': 'application/vnd.api+json',
    'accept': 'application/*, text/*',
    'authorization': 'Bearer ' + os.environ['TNYU_API_KEY_ADMIN']
}

# Reading data from the API
r = requests.get(TEST_BASE_URL + '/events',
                 headers=headers, verify=False)
data = json.loads(r.text)
print data

# Writing data to the API
event = {}
event['data'] = {}
event['data']['attributes'] = {}
event['data']['attributes']['title'] = 'Demo Event'
event['data']['type'] = 'questions'
event['data']['links'] = {}

event = json.dumps(event)
r = requests.post(TEST_BASE_URL + '/events',
                  data=event, headers=headers, verify=False)
data = json.loads(r.text)
print data

# Updating data to the API
# Update a resource 'event' with the id '5602db849a24fbd3eec8153f'
resource_type = 'events'
resource_id = '5602db849a24fbd3eec8153f'

# Make your small change
event = {}
event['id'] = resource_id
event['type'] = resource_type
event['attributes'] = {}
event['relationships'] = {}

event['attributes']['title'] = 'October DemoDays at VenmoHQ'

document = {}
document['data'] = event

document = json.dumps(document)

# Send a PUT request with the new data to the API
r = requests.patch(TEST_BASE_URL + '/events/5602db849a24fbd3eec8153f',
                   data=document, headers=headers, verify=False)
print r.text
