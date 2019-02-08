#combined.py
import time
import requests
import math
import random
from sense_hat import SenseHat


TOKEN = "..."  # Put your TOKEN here
DEVICE_LABEL = "machine"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here We need to change the variables here and in ubidots
VARIABLE_LABEL_2 = "humidity"  # Put your second variable label here
VARIABLE_LABEL_3 = "pressure"  # Put your second variable label here
#initialize your sensehat
sense = SenseHat()


def build_payload(variable_1, variable_2, variable_3):
    # Here's where we make changes:
    value_1 = sense.get_pressure()
    value_2 = sense.get_temperature()
    value_3 = sense.get_humidity()

    
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)