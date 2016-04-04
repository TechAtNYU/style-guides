# -*- coding: utf-8 -*-

# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os
import csv

BASE_URL = 'https://api.tnyu.org/v3'
TEST_BASE_URL = 'https://api.tnyu.org/v3-test'

EVENT_ID = '56d77321024bf852f5234c07'

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

# Print emails
rsvp_for_csv = []

for i in rsvps:
    to_append = {
        'name': i['attributes']['name'],
        'email': i['attributes']['contact']['email']
    }
    rsvp_for_csv.append(to_append)

csv_title = event['attributes']['title'].replace(' ', '_')

keys = rsvp_for_csv[0].keys()

with open(csv_title + '.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(rsvp_for_csv)
