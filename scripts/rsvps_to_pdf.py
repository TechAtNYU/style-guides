# -*- coding: utf-8 -*-

# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os
from TableFactory import *

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

# Print emails
rsvp_for_pdf = []

for i in rsvps:
    to_append = {
        'name': i['attributes']['name'],
        'email': i['attributes']['contact']['email'] if ('contact' in i['attributes'] and 'email' in i['attributes']['contact']) else ''
    }
    rsvp_for_pdf.append(to_append)

pdf_title = event['attributes']['title'].replace(' ', '_')

rowmaker = RowSpec(ColumnSpec('name', 'Name'),
                   ColumnSpec('email', 'Email'))
lines = rowmaker.makeall(rsvp_for_pdf)
pdfmaker = PDFTable('Attendees for ' +
                    event['attributes']['title'], headers=rowmaker)
open(pdf_title + '.pdf', 'wb').write(pdfmaker.render(lines))
