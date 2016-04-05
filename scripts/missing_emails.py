# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os

BASE_URL = 'https://api.tnyu.org/v3'
TEST_BASE_URL = 'https://api.tnyu.org/v3-test'

EVENT_ID = '56d501ed9ceb9b64d2b11ea2'

headers = {
    'content-type': 'application/vnd.api+json',
    'accept': 'application/*, text/*',
    'authorization': 'Bearer ' + os.environ['TNYU_API_KEY_ADMIN']
}

# Reading data from the API
r = requests.get(BASE_URL + '/people',
                 headers=headers, verify=False)

people = r.json()['data']

no_email = []

for person in people:
    if 'contact' not in person['attributes'] or 'email' not in person['attributes']['contact']:
        no_email.append(person)
