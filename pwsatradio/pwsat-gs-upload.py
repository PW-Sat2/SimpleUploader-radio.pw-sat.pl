#!/usr/bin/python

import sys
import json    
import requests
import time
import base64
import datetime

credentialsPath = "credentials.json"
baseUrl = 'http://pwsat2.softwaremill.com'
headers = {'content-type': 'application/json'}

def authenticate():
    credentials = loadCredentials(credentialsPath)
    url = baseUrl+'/api/authenticate'
    response = requests.post(url, data=json.dumps(credentials), headers=headers)
    return response.cookies;

def putPacket(cookies, full_frame):
    url = baseUrl+'/communication/frame'

    payload = { 'frame': full_frame[2],
                'timestamp': int(time.mktime(datetime.datetime.strptime(full_frame[0],
                "%Y-%m-%d_%H:%M:%S:%f").timetuple()))*1000,
                'traffic': 'Rx' if full_frame[1] == 'D' else 'Tx'}

    print "Payload:", payload
    response = requests.put(url, data=json.dumps(payload), headers=headers, cookies=cookies)
    return response.text;

def loadCredentials(path):
    with open(path) as f:
        credentials = json.load(f)
    return credentials


path = sys.argv[1]
with open(path, "rb") as f:
    for line in f:
        full_frame = line.split(',')
        print(putPacket(authenticate(), full_frame))
