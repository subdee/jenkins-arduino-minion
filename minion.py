#!/usr/bin/python

import serial
import time
import requests

latestBuildNumber = 0
jenkinsApiUrl = 'jenkinsapiurl'


def send_arduino_signal():
    arduino.write(bytes(b'1'))
    time.sleep(1)
    arduino.close()


while True:
    try:
        arduino = serial.Serial("/dev/ttyACM0")
        time.sleep(1)
        print("Connection to Arduino established successfully!\n")
    except Exception as e:
        print(e)

    try:
        response = requests.get(jenkinsApiUrl)
        status = response.json()
    except:
        print('Failed to parse JSON')

    if "result" in status:
        currentBuildNumber = status['number']
        print('checking build ' + str(currentBuildNumber))
        if status['result'] == "FAILURE" and currentBuildNumber > latestBuildNumber:
            send_arduino_signal()
            latestBuildNumber = status['number']
            print('build failed')
        elif status['result'] is None:
            print('build is running')
        elif status['result'] == "ABORTED":
            print('build was aborted')
        elif status['result'] == "SUCCESS":
            print('build is ok')
        else:
            print('build status unknown')

    time.sleep(30)
