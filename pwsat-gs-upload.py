#!/usr/bin/python

import sys
import json    
import requests
import time
import base64
import datetime

baseUrl = 'http://radio.pw-sat.pl'
headers = {'content-type': 'application/json'}

def authenticate(credentials_path):
    credentials = loadCredentials(credentials_path)
    url = baseUrl+'/api/authenticate'
    response = requests.post(url, data=json.dumps(credentials), headers=headers)
    return response.cookies;


def putPacket(cookies, full_frame):
    url = baseUrl+'/communication/frame'

    payload = { 'frame': full_frame[2],
                'timestamp': int(time.mktime(datetime.datetime.strptime(full_frame[0],
                "%Y-%m-%d_%H:%M:%S:%f").timetuple()))*1000,
                'traffic': 'Rx' if full_frame[1] == 'D' else 'Tx'}

    response = requests.put(url, data=json.dumps(payload), headers=headers, cookies=cookies)
    return response.text;


def loadCredentials(path):
    with open(path) as f:
        credentials = json.load(f)
    return credentials


credentials_path = sys.argv[1]
file_path = sys.argv[2]

with open(file_path, "rb") as f:
    for line in f:
        full_frame = line.split(',')
        print(putPacket(authenticate(credentials_path), full_frame))
