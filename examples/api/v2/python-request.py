# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests

import requests, json

headers = {'content-type': 'application/vnd.api+json', 'accept': 'application/*, text/*', 'x-api-key': os.environ['TNYU_API_KEY']}
r = requests.get('https://api.tnyu.org/v2/events', headers=headers, verify=False)
data = json.loads(r.text)

# All events
# print data['data']

# Title of the first event that's returned from the API
# print data['data'][0]['title']

# Printing out all the titles
for i in data['data']:
    print i['title']
