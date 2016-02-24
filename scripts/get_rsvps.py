# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os

BASE_URL = 'https://api.tnyu.org/v3'
TEST_BASE_URL = 'https://api.tnyu.org/v3-test'

EVENT_ID = '56c29c57e7afddface1d78c8'

headers = {
    'content-type': 'application/vnd.api+json',
    'accept': 'application/*, text/*',
    'authorization': 'Bearer ' + os.environ['TNYU_API_KEY_ADMIN']
}

# Reading data from the API
r = requests.get(BASE_URL + '/events/' + EVENT_ID + '?include=rsvps',
                 headers=headers, verify=False)
data = json.loads(r.text)
event = data['data']
rsvps = data['included']

peopleIdToPeople = {}
for i in rsvps:
    peopleIdToPeople[i['id']] = i

# ... further processing if needed

# Print emails
for i in rsvps:
    print i['attributes']['contact']['email']
