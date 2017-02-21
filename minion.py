#!/usr/bin/python

import serial
import time
import requests
import sys

try:
    arduino = serial.Serial("/dev/ttyACM0")
    time.sleep(1)
    print("Connection to Arduino established successfully!\n")
except Exception as e:
    print(e)

latestBuildNumber = None
jenkinsApiUrl = 'jenkinsapiurl';

while True:
    try:
        response = requests.get()
        status = response.json()
    except:
        print('Failed to parse JSON')
        sys.exit(3)

    if "result" in status:
        currentBuildNumber = status['number']
        print('checking build ' + str(currentBuildNumber))
        if status['result'] != "SUCCESS" and currentBuildNumber > latestBuildNumber:
            arduino.write(bytes(b'1'))
            time.sleep(1)
            arduino.close()
            latestBuildNumber = status['number']
            print('build failed')
        else:
            print('build succeeded')

    time.sleep(60)
