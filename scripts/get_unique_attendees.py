import requests
import json
import os
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Removing requests warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_URL = 'https://api.tnyu.org/v3'
TEST_BASE_URL = 'https://api.tnyu.org/v3-test'

headers = {
    'content-type': 'application/vnd.api+json',
    'accept': 'application/*, text/*',
    'authorization': 'Bearer ' + os.environ['TNYU_API_KEY_ADMIN']
}
events = [
        '56eacca4af7309928af4ea5a', # demoday
        '56d5036841f94b11ad9cd3ce', # tech mixer
        '56d5030a4ba7f9bb27085b76', # keynote
        '56d507d93aaf19a04dd684e1', # PM panel
        '56d5017c174daa0cd334b004', # hackstories
        '56d500e9d31fc80860ad5ab0', # CEO talks
        '56d501ed9ceb9b64d2b11ea2', # working as a designer
        '56d4fe3ee28ed76ab27fa697', # diversity panel
        '56d77321024bf852f5234c07', # business careers
        '56d4fd58bc0e51298ced2900', # webscraping
        ]

def get_unique_attendees(master, EVENT_ID):
    count = 0
    r = requests.get(BASE_URL + '/events/' + EVENT_ID, headers=headers,
            verify=False).json()['data']
    for attendee in r['relationships']['attendees']['data']:
        if is_recurring(master, attendee['id']):
            count+=1
    print r['attributes']['title']
    print count


def is_recurring(master, personId):
    p = len(master) - 11
    recurring = False
    for event in master[0:p]:
        attendees = event['relationships']['attendees']['data']
        for attendee in attendees:
            if attendee['id'] == personId:
                recurring = True
                break
    return recurring

def showedup_more_than_once(sw, current_eid, personId):
    showed = 0
    for event in sw:
        if event['id'] != current_eid:
            attendees = event['relationships']['attendees']['data']
            for attendee in attendees:
                if attendee['id'] == personId:
                    showed+=1
    return showed

master = requests.get(BASE_URL + '/events?sort=startDateTime', headers=headers,
        verify=False).json()['data']

p = len(master) - 11
startup_week = master[p:]
# print json.dumps(startup_week[0], indent=2)

# for eid in events:
#     get_unique_attendees(master, eid)

attendance = {}
for sw_event in startup_week:
    attendees = sw_event['relationships']['attendees']['data']
    for attendee in attendees:
        if attendance.get(attendee['id']) is None:
            attendance[attendee['id']] = 0
        attendance[attendee['id']]+=1

count = 0
for key in attendance:
    if attendance[key] > 4:
        print json.dumps(attendance[key], indent=2)
        count+=1
print
print count
