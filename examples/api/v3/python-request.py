# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests
import json
import os

headers = {
    'content-type': 'application/vnd.api+json',
    'accept': 'application/*, text/*',
    'authorization': 'Bearer ' + os.environ['TNYU_API_KEY']
}

r = requests.get('https://api.tnyu.org/v3/events',
                 headers=headers, verify=False)
data = json.loads(r.text)
print data
